import grpc
import pm_pb2
import pm_pb2_grpc

def menu():
    print("Escolha uma operação:")
    print("1. Adicionar Professor à Disciplina")
    print("2. Remover Professor da Disciplina")
    print("3. Adicionar Aluno à Disciplina")
    print("4. Remover Aluno da Disciplina")
    print("5. Detalhar Disciplina")
    print("6. Obter Disciplinas do Professor")
    print("7. Obter Disciplinas do Aluno")
    print("0. Sair")

def main():
    channel = grpc.insecure_channel('localhost:50051')
    stub = pm_pb2_grpc.PortalMatriculaStub(channel)

    while True:
        menu()
        escolha = input("Digite o número da operação desejada: ")

        if escolha == "1":
            disciplina = input("Digite a sigla da disciplina: ")
            siape = input("Digite o SIAPE do professor: ")
            response = stub.AdicionaProfessor(pm_pb2.DisciplinaPessoa(disciplina=disciplina, idPessoa=siape))
            print(response.msg)

        elif escolha == "2":
            disciplina = input("Digite a sigla da disciplina: ")
            siape = input("Digite o SIAPE do professor a ser removido: ")
            response = stub.RemoveProfessor(pm_pb2.DisciplinaPessoa(disciplina=disciplina, idPessoa=siape))
            print(response.msg)

        elif escolha == "3":
            disciplina = input("Digite a sigla da disciplina: ")
            matricula = input("Digite a matrícula do aluno: ")
            response = stub.AdicionaAluno(pm_pb2.DisciplinaPessoa(disciplina=disciplina, idPessoa=matricula))
            print(response.msg)

        elif escolha == "4":
            disciplina = input("Digite a sigla da disciplina: ")
            matricula = input("Digite a matrícula do aluno a ser removido: ")
            response = stub.RemoveAluno(pm_pb2.DisciplinaPessoa(disciplina=disciplina, idPessoa=matricula))
            print(response.msg)

        elif escolha == "5":
            disciplina = input("Digite a sigla da disciplina: ")
            response = stub.DetalhaDisciplina(pm_pb2.Identificador(id=disciplina))
            print(f"Disciplina: {response.disciplina.nome}")
            if response.professor:
                print(f"Professor: {response.professor.nome}")
            print("Alunos:")
            for aluno in response.alunos:
                print(f"  - Matrícula: {aluno.matricula}, Nome: {aluno.nome}")

        elif escolha == "6":
            siape = input("Digite o SIAPE do professor: ")
            response = stub.ObtemDisciplinasProfessor(pm_pb2.Identificador(id=siape))
            for disciplina in response:
                print(f"Disciplina: {disciplina.disciplina.nome}, Total de Alunos: {disciplina.totalAlunos}")

        elif escolha == "7":
            matricula = input("Digite a matrícula do aluno: ")
            response = stub.ObtemDisciplinasAluno(pm_pb2.Identificador(id=matricula))
            for disciplina in response:
                print(f"Disciplina: {disciplina.disciplina.nome}, Professor: {disciplina.professor.nome}")

        elif escolha == "0":
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    main()