import grpc
import paho.mqtt.client as mqtt
import json
import uuid

from concurrent import futures

import pa_pb2
import pa_pb2_grpc

myuuid = uuid.uuid4()
print('Your UUID is: ' + str(myuuid))

class ServicoPortalAdministrativo(pa_pb2_grpc.PortalAdministrativoServicer):
    def __init__(self):
        self.updated = 0
        self.alunos = {}
        self.professores = {}
        self.disciplinas = {}

        # Adiciona a logica de subscription
        self.client = mqtt.Client()
        self.client.connect("localhost", 1883)
        self.client.subscribe("servers_adm")
        self.client.on_message = self.on_message
        self.client.loop_start()

        # Tenta se atualizar com os outros servidores que já estavam em execucao
        msg = json.dumps({"uuid": str(myuuid), "mode": "GET"})
        self.publicar_mensagem_adm(msg)

    def publicar_mensagem_adm(self, mensagem):
        self.client.publish("servers_adm", mensagem)

    def publicar_mensagem_mat(self, mensagem):
        self.client.publish("servers_mat", mensagem)

    # Interpreta as mensagens recebidas pelos outros portais.
    #
    def on_message(self, client, userdata, msg):
        contents = json.loads(msg.payload)
        if contents['uuid'] != str(myuuid):
            print(f"Mensagem recebida de outro portal: {contents}")

            # Mode = POST / PUT / DELETE / GET / SERVER_UPDATE
            #     Indica a operação a ser feita
            # Type = 0 (Aluno) / 1 (Professor) / 2 (Disciplina)
            #     Indica o tipo de dado que é feita a operação

            # Para criar um dado
            if contents['mode'] == "POST":
                if contents['type'] == 0:
                    print(f"Ordens: Criar aluno {contents['nome']} de matricula {contents['id']}")
                    res = self.NovoAluno(pa_pb2.Aluno(matricula=contents['id'],
                                                      nome=contents['nome']), None)
                    print(res.msg)
                elif contents['type'] == 1:
                    print(f"Criar professor {contents['nome']} de siape {contents['id']}")
                    res = self.NovoProfessor(pa_pb2.Professor(siape=contents['id'],
                                                              nome=contents['nome']), None)
                    print(res.msg)
                elif contents['type'] == 2:
                    print(f"Criar disciplina {contents['nome']}" + 
                          f" de sigla {contents['id']} com {contents['id']} vagas")
                    res = self.NovaDisciplina(pa_pb2.Disciplina(sigla=contents['id'],
                                                                nome=contents['nome']), None)
                    print(res.msg)

            # Para modificar algum dado
            elif contents['mode'] == "PUT":
                if contents['type'] == 0:
                    print(f"Modificar nome do aluno de matricula {contents['id']} para {contents['nome']}")
                    res = self.EditaAluno(pa_pb2.Aluno(matricula=contents['id'],
                                                       nome=contents['nome']), None)
                    print(res.msg)
                elif contents['type'] == 1:
                    print(f"Modificar nome do professor de siape {contents['id']} para {contents['nome']}")
                    print(f"Criar professor {contents['nome']} de siape {contents['id']}")
                    res = self.EditaProfessor(pa_pb2.Professor(siape=contents['id'],
                                                              nome=contents['nome']), None)
                    print(res.msg)
                elif contents['type'] == 2:
                    print(f"Modificar nome da disciplina de sigla {contents['id']} para {contents['nome']}")
                    res = self.EditaDisciplina(pa_pb2.Disciplina(sigla=contents['id'],
                                                                nome=contents['nome']), None)
                    print(res.msg)

            # Para apagar alguma informação
            elif contents['mode'] == "DELETE":
                if contents['type'] == 0:
                    print(f"Remover aluno de matricula {contents['id']}")
                    res = self.RemoveAluno(pa_pb2.Identificador(id=contents['id']), None)
                    print(res.msg)
                elif contents['type'] == 1:
                    print(f"Remover professor de siape {contents['id']}")
                    res = self.RemoveProfessor(pa_pb2.Identificador(id=contents['id']), None)
                    print(res.msg)
                elif contents['type'] == 2:
                    print(f"Remover disciplina de sigla {contents['id']}")
                    res = self.RemoveDisciplina(pa_pb2.Identificador(id=contents['id']), None)
                    print(res.msg)

            # Para atualizar outro portal
            elif contents['mode'] == "GET":
                ## Teste de Integração com portal de Matrícula
                # if contents['source'] == "mat":
                #     if contents['type'] == 0:
                #         print(f"Consultar aluno de matricula {contents['id']}")
                #         res = self.RemoveAluno(pa_pb2.Identificador(id=contents['id']), None)
                #         print(res.msg)
                #     elif contents['type'] == 1:
                #         print(f"Consultar professor de siape {contents['id']}")
                #         res = self.RemoveProfessor(pa_pb2.Identificador(id=contents['id']), None)
                #         print(res.msg)
                #     elif contents['type'] == 2:
                #         print(f"Consultar disciplina de sigla {contents['id']}")
                #         res = self.RemoveDisciplina(pa_pb2.Identificador(id=contents['id']), None)
                #         print(res.msg)
                # else:
                    print("get")
                    msg = json.dumps({"uuid": str(myuuid), "mode": "SERVER_UPDATE", "alunos": self.alunos,
                                      "professores": self.professores, "disciplinas": self.disciplinas})
                    self.publicar_mensagem_adm(msg)

            elif contents['mode'] == "SERVER_UPDATE" and self.updated == 0:
                print("Fazendo update no banco de dados local.")
                in_alunos = contents['alunos']
                in_professores = contents['professores']
                in_disciplinas = contents['disciplinas']
                for aluno in in_alunos:
                    res = self.NovoAluno(pa_pb2.Aluno(matricula=aluno,
                                                      nome=in_alunos[aluno]), None)
                    print(res.msg)
                for professor in in_professores:
                    res = self.NovoProfessor(pa_pb2.Professor(siape=professor,
                                                              nome=in_professores[professor]), None)
                    print(res.msg)

                for disciplina in in_disciplinas:
                    res = self.NovaDisciplina(pa_pb2.Disciplina(sigla=disciplina,
                                                                nome=in_disciplinas[disciplina]), None)
                    print(res.msg)
                self.updated = 1
                print("Update do banco de dados local finalizado.")

        else:
            print(f"Mensagem publicada: {contents}")

    def NovoAluno(self, request, context):
        if len(request.matricula) > 4 and len(request.nome) > 4:
            if request.matricula not in self.alunos:
                self.alunos[request.matricula] = request.nome
                if context != None:
                    msg = json.dumps({"uuid": str(myuuid), "mode": "POST", "type": 0,
                                      "nome": request.nome, "id": request.matricula})
                    self.publicar_mensagem_adm(msg)
                return pa_pb2.Status(status=0, msg="Aluno cadastrado com sucesso")
            else:
                return pa_pb2.Status(status=1, msg="Aluno já cadastrado")
        else:
            return pa_pb2.Status(status=1, msg="Matrícula e nome devem ter mais de 4 caracteres")

    def EditaAluno(self, request, context):
        if len(request.matricula) > 4 and len(request.nome) > 4:
            if request.matricula in self.alunos:
                self.alunos[request.matricula] = request.nome
                if context != None:
                    msg = json.dumps({"uuid": str(myuuid), "mode": "PUT", "type": 0,
                                      "nome": request.nome, "id": request.matricula})
                    self.publicar_mensagem_adm(msg)
                return pa_pb2.Status(status=0, msg="Aluno editado com sucesso")
            else:
                return pa_pb2.Status(status=1, msg="Aluno não encontrado")
        else:
            return pa_pb2.Status(status=1, msg="Matrícula e nome devem ter mais de 4 caracteres")

    def RemoveAluno(self, request, context):
        if request.id in self.alunos:
            del self.alunos[request.id]
            if context != None:
                msg = json.dumps({"uuid": str(myuuid), "mode": "DELETE", "type": 0, "id": request.id})
                self.publicar_mensagem_adm(msg)
            return pa_pb2.Status(status=0, msg="Aluno removido com sucesso")
        else:
            return pa_pb2.Status(status=1, msg="Aluno não encontrado")

    def ObtemAluno(self, request, context):
        if request.id in self.alunos:
            return pa_pb2.Aluno(matricula=request.id, nome=self.alunos[request.id])
        else:
            return pa_pb2.Aluno()

    def ObtemTodosAlunos(self, request, context):
        for matricula, nome in self.alunos.items():
            yield pa_pb2.Aluno(matricula=matricula, nome=nome)

    def NovoProfessor(self, request, context):
        if len(request.siape) > 4 and len(request.nome) > 4:
            if request.siape not in self.professores:
                self.professores[request.siape] = request.nome
                if context != None:
                    msg = json.dumps({"uuid": str(myuuid), "mode": "POST", "type": 1,
                                      "nome": request.nome, "id": request.siape})
                    self.publicar_mensagem_adm(msg)
                return pa_pb2.Status(status=0, msg="Professor cadastrado com sucesso")
            else:
                return pa_pb2.Status(status=1, msg="Professor já cadastrado")
        else:
            return pa_pb2.Status(status=1, msg="Siape e nome devem ter mais de 4 caracteres")

    def EditaProfessor(self, request, context):
        if len(request.siape) > 4 and len(request.nome) > 4:
            if request.siape in self.professores:
                self.professores[request.siape] = request.nome
                if context != None:
                    msg = json.dumps({"uuid": str(myuuid), "mode": "PUT", "type": 1,
                                      "nome": request.nome, "id": request.siape})
                    self.publicar_mensagem_adm(msg)
                return pa_pb2.Status(status=0, msg="Professor editado com sucesso")
            else:
                return pa_pb2.Status(status=1, msg="Professor não encontrado")
        else:
            return pa_pb2.Status(status=1, msg="Siape e nome devem ter mais de 4 caracteres")

    def RemoveProfessor(self, request, context):
        if request.id in self.professores:
            del self.professores[request.id]
            if context != None:
                msg = json.dumps({"uuid": str(myuuid), "mode": "DELETE", "type": 1, "id": request.id})
                self.publicar_mensagem_adm(msg)
            return pa_pb2.Status(status=0, msg="Professor removido com sucesso")
        else:
            return pa_pb2.Status(status=1, msg="Professor não encontrado")

    def ObtemProfessor(self, request, context):
        if request.id in self.professores:
            return pa_pb2.Professor(siape=request.id, nome=self.professores[request.id])
        else:
            return pa_pb2.Professor()

    def ObtemTodosProfessores(self, request, context):
        for siape, nome in self.professores.items():
            yield pa_pb2.Professor(siape=siape, nome=nome)

    def NovaDisciplina(self, request, context):
        if len(request.sigla) > 4 and len(request.nome) > 4:
            if request.sigla not in self.disciplinas:
                self.disciplinas[request.sigla] = request.nome
                if context != None:
                    msg = json.dumps({"uuid": str(myuuid), "mode": "POST",
                                       "type": 2,"nome": request.nome,
                                       "id": request.sigla,"vagas": request.vagas})
                    self.publicar_mensagem_adm(msg)
                return pa_pb2.Status(status=0, msg="Disciplina cadastrada com sucesso")
            else:
                return pa_pb2.Status(status=1, msg="Disciplina já cadastrada")
        else:
            return pa_pb2.Status(status=1, msg="Sigla e nome devem ter mais de 4 caracteres")

    def EditaDisciplina(self, request, context):
        if len(request.sigla) > 4 and len(request.nome) > 4:
            if request.sigla in self.disciplinas:
                self.disciplinas[request.sigla] = request.nome
                if context != None:
                    msg = json.dumps({"uuid": str(myuuid), "mode": "PUT", "type": 2,
                                      "nome": request.nome, "id": request.sigla,
                                      "vagas": request.vagas})
                    self.publicar_mensagem_adm(msg)
                return pa_pb2.Status(status=0, msg="Disciplina editada com sucesso")
            else:
                return pa_pb2.Status(status=1, msg="Disciplina não encontrada")
        else:
            return pa_pb2.Status(status=1, msg="Sigla e nome devem ter mais de 4 caracteres")

    def RemoveDisciplina(self, request, context):
        if request.id in self.disciplinas:
            del self.disciplinas[request.id]
            if context != None:
                msg = json.dumps({"uuid": str(myuuid), "mode": "DELETE", "type": 2, "id": request.id})
                self.publicar_mensagem_adm(msg)
            return pa_pb2.Status(status=0, msg="Disciplina removida com sucesso")
        else:
            return pa_pb2.Status(status=1, msg="Disciplina não encontrada")

    def ObtemDisciplina(self, request, context):
        if request.id in self.disciplinas:
            return pa_pb2.Disciplina(sigla=request.id, nome=self.disciplinas[request.id])
        else:
            return pa_pb2.Disciplina()

    def ObtemTodasDisciplinas(self, request, context):
        for sigla, nome in self.disciplinas.items():
            yield pa_pb2.Disciplina(sigla=sigla, nome=nome)


def servir():
    port = input("Insira porta do servidor: ")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pa_pb2_grpc.add_PortalAdministrativoServicer_to_server(
        ServicoPortalAdministrativo(), server)
    server.add_insecure_port(f"[::]:{port}")
    server.start()
    print(f"Servidor do Portal Administrativo iniciado na porta {port}. Aguardando conexões...")
    server.wait_for_termination()


if __name__ == '__main__':
    servir()
