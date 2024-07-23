Algoritmo "TestAlgoritm"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 23/07/2024
Var
// Seção de Declarações das variáveis

    sexo:caractere
    altura : real
    pesoIdeal: real
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc...
    // Entrada: obtendo o sexo do usuário
    escreva ("Insira o gênero (M ou F):" )
    leia (sexo)

    // Entrada: obtendo a altura do usuário
    escreva ("Insira a altura em cm:")
       leia(altura)

    //Calcula o peso ideal com base no sexo
    Se sexo = ("M") entao
        pesoIdeal <- (altura * 0.95) - 95
    senao

            pesoIdeal <- (altura * 0.85) - 85
       // senao
          //  Escreva ("Sexo inválido. Digite 'masculino' ou 'feminino'." )

        //Fimse
    fimse

    //Saída: imprime o peso ideal
    escreva ("O peso ideal para uma pessoa do sexo", sexo, "e altura", altura, "cm", pesoIdeal, "kg.")


Fimalgoritmo