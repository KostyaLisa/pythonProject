Algoritmo "TestAlgoritm"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 23/07/2024
Var
// Se��o de Declara��es das vari�veis

    sexo:caractere
    altura : real
    pesoIdeal: real
Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc...
    // Entrada: obtendo o sexo do usu�rio
    escreva ("Insira o g�nero (M ou F):" )
    leia (sexo)

    // Entrada: obtendo a altura do usu�rio
    escreva ("Insira a altura em cm:")
       leia(altura)

    //Calcula o peso ideal com base no sexo
    Se sexo = ("M") entao
        pesoIdeal <- (altura * 0.95) - 95
    senao

            pesoIdeal <- (altura * 0.85) - 85
       // senao
          //  Escreva ("Sexo inv�lido. Digite 'masculino' ou 'feminino'." )

        //Fimse
    fimse

    //Sa�da: imprime o peso ideal
    escreva ("O peso ideal para uma pessoa do sexo", sexo, "e altura", altura, "cm", pesoIdeal, "kg.")


Fimalgoritmo