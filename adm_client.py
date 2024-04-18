import grpc
import pa_pb2
import pa_pb2_grpc

def menu():

    print("\n\n================================")
    print("\nEscolha uma operação:")
    print("1. Novo Aluno")
    print("2. Editar Aluno")
    print("3. Remover Aluno")
    print("4. Obter Aluno")
    print("5. Obter Todos Alunos")
    print("6. Novo Professor")
    print("7. Editar Professor")
    print("8. Remover Professor")
    print("9. Obter Professor")
    print("10. Obter Todos Professores")
    print("11. Nova Disciplina")
    print("12. Editar Disciplina")
    print("13. Remover Disciplina")
    print("14. Obter Disciplina")
    print("15. Obter Todas Disciplinas")
    print("0. Sair\n")


def main():
    port = input("Insira a porta do Portal Administrativo que deseja se conectar: ")
    channel = grpc.insecure_channel(f"localhost:{port}")
    stub = pa_pb2_grpc.PortalAdministrativoStub(channel)

    while True:
        menu()
        escolha = input("Digite o número da operação desejada: ")

        if escolha == "1":
            matricula = input("Digite a matrícula do aluno: ")
            nome = input("Digite o nome do aluno: ")
            response = stub.NovoAluno(pa_pb2.Aluno(matricula=matricula, nome=nome))
            print(response.msg)

        elif escolha == "2":
            matricula = input("Digite a matrícula do aluno a ser editado: ")
            nome = input("Digite o novo nome do aluno: ")
            response = stub.EditaAluno(pa_pb2.Aluno(matricula=matricula, nome=nome))
            print(response.msg)

        elif escolha == "3":
            matricula = input("Digite a matrícula do aluno a ser removido: ")
            response = stub.RemoveAluno(pa_pb2.Identificador(id=matricula))
            print(response.msg)

        elif escolha == "4":
            matricula = input("Digite a matrícula do aluno a ser obtido: ")
            response = stub.ObtemAluno(pa_pb2.Identificador(id=matricula))
            if response.matricula:
                print(f"Matrícula: {response.matricula}, Nome: {response.nome}")
            else:
                print("Aluno não encontrado.")

        elif escolha == "5":
            response = stub.ObtemTodosAlunos(pa_pb2.Vazia())
            for aluno in response:
                print(f"Matrícula: {aluno.matricula}, Nome: {aluno.nome}")

        elif escolha == "6":
            siape = input("Digite o SIAPE do professor: ")
            nome = input("Digite o nome do professor: ")
            response = stub.NovoProfessor(pa_pb2.Professor(siape=siape, nome=nome))
            print(response.msg)

        elif escolha == "7":
            siape = input("Digite o SIAPE do professor a ser editado: ")
            nome = input("Digite o novo nome do professor: ")
            response = stub.EditaProfessor(pa_pb2.Professor(siape=siape, nome=nome))
            print(response.msg)

        elif escolha == "8":
            siape = input("Digite o SIAPE do professor a ser removido: ")
            response = stub.RemoveProfessor(pa_pb2.Identificador(id=siape))
            print(response.msg)

        elif escolha == "9":
            siape = input("Digite o SIAPE do professor a ser obtido: ")
            response = stub.ObtemProfessor(pa_pb2.Identificador(id=siape))
            if response.siape:
                print(f"SIAPE: {response.siape}, Nome: {response.nome}")
            else:
                print("Professor não encontrado.")

        elif escolha == "10":
            response = stub.ObtemTodosProfessores(pa_pb2.Vazia())
            for professor in response:
                print(f"SIAPE: {professor.siape}, Nome: {professor.nome}")

        elif escolha == "11":
            sigla = input("Digite a sigla da disciplina: ")
            nome = input("Digite o nome da disciplina: ")
            vagas = input("Digite a quantidade de vagas da disciplina: ")
            response = stub.NovaDisciplina(pa_pb2.Disciplina(sigla=sigla, nome=nome, vagas=vagas))
            print(response.msg)

        elif escolha == "12":
            sigla = input("Digite a sigla da disciplina a ser editada: ")
            nome = input("Digite o novo nome da disciplina: ")
            response = stub.EditaDisciplina(pa_pb2.Disciplina(sigla=sigla, nome=nome))
            print(response.msg)

        elif escolha == "13":
            sigla = input("Digite a sigla da disciplina a ser removida: ")
            response = stub.RemoveDisciplina(pa_pb2.Identificador(id=sigla))
            print(response.msg)

        elif escolha == "14":
            sigla = input("Digite a sigla da disciplina a ser obtida: ")
            response = stub.ObtemDisciplina(pa_pb2.Identificador(id=sigla))
            if response.sigla:
                print(f"Sigla: {response.sigla}, Nome: {response.nome}")
            else:
                print("Disciplina não encontrada.")

        elif escolha == "15":
            response = stub.ObtemTodasDisciplinas(pa_pb2.Vazia())
            for disciplina in response:
                print(f"Sigla: {disciplina.sigla}, Nome: {disciplina.nome}")

        elif escolha == "0":
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == '__main__':
    main()
