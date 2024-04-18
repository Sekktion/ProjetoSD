import grpc
import paho.mqtt.client as mqtt
import json
import uuid
from concurrent import futures

import pm_pb2
import pm_pb2_grpc

myuuid = uuid.uuid4()
print('Your UUID is: ' + str(myuuid))

class ServicoPortalMatricula(pm_pb2_grpc.PortalMatriculaServicer):
    def __init__(self):
        self.alunos = {}
        self.professores = {}
        self.disciplinas = {}

        # Adiciona a lógica de assinatura
        self.client = mqtt.Client()
        self.client.connect("localhost", 1883)
        self.client.subscribe("admin_topic")
        self.client.on_message = self.on_message
        self.client.loop_start()

    def publicar_mensagem(self, mensagem):
        self.client.publish("mat_topic", mensagem)

    def on_message(self, client, userdata, msg):
        print(f"Recebido do 'admin_topic': {msg.payload}")
        
    ## WIP
    def AdicionaProfessor(self, request):
        siape = request.idPessoa
        disciplina = request.disciplina
        
        if disciplina in self.disciplinas:
            if siape in self.professores:
                self.disciplinas[disciplina] = siape
                self.publicar_mensagem("Novo professor adicionado à disciplina")
                return pm_pb2.Status(status=0, msg="Professor adicionado com sucesso")
            else:
                return pm_pb2.Status(status=1, msg="Professor já associado à disciplina")
        else:
            return pm_pb2.Status(status=1, msg="Disciplina não encontrada")

    def RemoveProfessor(self, request, context):
        disciplina = request.disciplina
        siape = request.idPessoa

        if disciplina in self.disciplinas:
            if siape in self.professores:
                del self.professores[siape]
                self.publicar_mensagem("Professor removido da disciplina")
                return pm_pb2.Status(status=0, msg="Professor removido com sucesso")
            else:
                return pm_pb2.Status(status=1, msg="Professor não encontrado na disciplina")
        else:
            return pm_pb2.Status(status=1, msg="Disciplina não encontrada")

    def AdicionaAluno(self, request, context):
        disciplina = request.disciplina
        matricula = request.idPessoa

        if disciplina in self.disciplinas:
            if matricula not in self.alunos:
                self.alunos[matricula] = request.idPessoa
                self.publicar_mensagem("Aluno adicionado a disciplina")
                return pm_pb2.Status(status=0, msg="Aluno adicionado com sucesso")
            else:
                return pm_pb2.Status(status=1, msg="Aluno já matriculado na disciplina")
        else:
            return pm_pb2.Status(status=1, msg="Disciplina não encontrada")

    def RemoveAluno(self, request, context):
        disciplina = request.disciplina
        matricula = request.idPessoa

        if disciplina in self.disciplinas:
            if matricula in self.alunos:
                del self.alunos[matricula]
                self.publicar_mensagem("Aluno removido da disciplina")
                return pm_pb2.Status(status=0, msg="Aluno removido com sucesso")
            else:
                return pm_pb2.Status(status=1, msg="Aluno não encontrado na disciplina")
        else:
            return pm_pb2.Status(status=1, msg="Disciplina não encontrada")

    def DetalhaDisciplina(self, request, context):
        sigla = request.id
        if sigla in self.disciplinas:
            disciplina = self.disciplinas[sigla]
            professor = self.professores.get(sigla, None)
            alunos = [aluno for aluno in self.alunos.values() if aluno.disciplina == sigla]

            relatorio = pm_pb2.RelatorioDisciplina(
                disciplina=disciplina,
                professor=professor,
                alunos=alunos
            )

            return relatorio
        else:
            return pm_pb2.RelatorioDisciplina()

    def ObtemDisciplinasProfessor(self, request, context):
        siape = request.id
        disciplinas_associadas = [
            pm_pb2.ResumoDisciplina(
                disciplina=disciplina,
                professor=self.professores[disciplina.sigla],
                totalAlunos=len([aluno for aluno in self.alunos.values() if aluno.disciplina == disciplina.sigla])
            )
            for disciplina in self.disciplinas.values()
            if self.professores.get(disciplina.sigla, None) == siape
        ]

        for disciplina_associada in disciplinas_associadas:
            yield disciplina_associada

    def ObtemDisciplinasAluno(self, request, context):
        matricula = request.id
        disciplinas_associadas = [
            pm_pb2.ResumoDisciplina(
                disciplina=aluno.disciplina,
                professor=self.professores.get(aluno.disciplina, None),
                totalAlunos=len([aluno for aluno in self.alunos.values() if aluno.disciplina == aluno.disciplina])
            )
            for aluno in self.alunos.values()
            if aluno.matricula == matricula
        ]

        for disciplina_associada in disciplinas_associadas:
            yield disciplina_associada


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pm_pb2_grpc.add_PortalMatriculaServicer_to_server(ServicoPortalMatricula(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()