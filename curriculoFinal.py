def coletarDados():
    foto = input("Digite a URL da sua foto de perfil: ")
    nome = input("Digite seu nome completo: ")
    email = input("Digite seu e-mail: ")
    telefone = input("Digite seu telefone: ")
    endereco = input("Digite seu endereço: ")
    resumo = input("Digite um resumo sobre você: ")

    formacoes = []
    print("\nDigite suas formações acadêmicas (digite 'sair' para finalizar):")
    while True:
        formacao = input("Formação: ")
        if formacao.lower() == 'sair':
            break
        formacoes.append(formacao)
        
    experiencias = []
    print("\nDigite suas experiências profissionais (digite 'sair' para finalizar):")
    while True:
        experiencia = input("Experiência: ")
        if experiencia.lower() == 'sair':
            break
        experiencias.append(experiencia)
        
    habilidades = []
    print("\nDigite suas habilidades (digite 'sair' para finalizar):")
    while True:
        habilidade = input("Habilidade: ")
        if habilidade.lower() == 'sair':
            break
        habilidades.append(habilidade)
    return nome, email, telefone, endereco, resumo, formacoes, experiencias, foto, habilidades

def gerarCurriculo(nome, email, telefone, endereco, resumo, formacoes, experiencias, foto, habilidades):
    formacoesEmHtml = ""
    contador = 0
    while contador < len(formacoes):
        formacaoAtual = formacoes[contador]
        formacoesEmHtml += f"<li>{formacaoAtual}</li>"
        contador += 1

    experienciasEmHtml = ""
    contador = 0
    while contador < len(experiencias):
        experienciaAtual = experiencias[contador]
        experienciasEmHtml += f"<li>{experienciaAtual}</li>"
        contador += 1

    habilidadesEmHtml = ""
    contador = 0
    while contador < len(habilidades):
        habilidadeAtual = habilidades[contador]
        habilidadesEmHtml += f"<li>{habilidadeAtual}</li>"
        contador += 1

    htmlFinal = f""" 

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Currículo</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 30px 15px;
            background: linear-gradient(135deg, rgb(245, 234, 255), rgb(234, 220, 255));
            color: rgb(75, 59, 90);
        }}
        .container {{
            max-width: 800px;
            margin: 20px auto;
            background-color: rgb(255, 255, 255);
            padding: 30px;
            border-radius: 25px;
            box-shadow: 0 8px 25px rgba(126, 87, 155, 0.18);
        }}
        .cabecalho {{
            text-align: center;
            background-color: rgb(243, 232, 255);
            padding: 25px;
            border-radius: 20px;
        }}
        .foto-perfil {{
            width: 150px;
            height: 150px;
            border-radius: 50%;
            object-fit: cover;
            border: 5px solid rgb(216, 180, 254);
            box-shadow: 0 5px 15px rgba(126, 87, 155, 0.2);
        }}
        h1 {{
            margin-top: 15px;
            margin-bottom: 8px;
            color: rgb(124, 58, 237);
            font-size: 32px;
        }}
        .contato {{
            color: rgb(107, 90, 120);
            margin: 0;
        }}
        .secao {{
            margin-top: 30px;
            padding: 20px;
            background-color: rgb(250, 247, 255);
            border-radius: 18px;
            border-left: 5px solid rgb(192, 132, 252);
        }}
        h2 {{
            color: rgb(124, 58, 237);
            border-bottom: 2px solid rgb(233, 213, 255);
            padding-bottom: 8px;
            margin-top: 0;
        }}
        p {{
            line-height: 1.6;
        }}
        ul {{
            list-style-type: none;
            padding-left: 0;
        }}
        li {{
            background-color: rgb(240, 231, 255);
            margin: 8px 0;
            padding: 10px 15px;
            border-radius: 12px;
            color: rgb(91, 70, 112);
        }}
        li::before {{
            content: "♡ ";
            color: rgb(168, 85, 247);
            font-weight: bold;
        }}

    </style>
</head>
<body>
    <div class="container">
       <div class="cabecalho">
            <img class="foto-perfil" src="{foto}" alt="Foto de Perfil">
            <h1>{nome}</h1>
            <p class="contato"> Email: {email} </p>
            <p class="contato"> Telefone: {telefone} </p>
            <p class="contato">  Endereço: {endereco} </p>
        </div>
        
        <div class="secao">
            <h2>Resumo Pessoal</h2>
            <p>{resumo}</p>
        </div>

        <div class="secao">
            <h2>Formação Acadêmica</h2>
            <ul> {formacoesEmHtml} </ul>
        </div>

        <div class="secao">
            <h2>Experiência Profissional</h2>
            <ul> {experienciasEmHtml} </ul>
        </div>

        <div class="secao">
            <h2>Habilidades</h2>
            <ul> {habilidadesEmHtml} </ul>
        </div>
    </div>
</body>
</html>
"""
    return htmlFinal

def salvarCurriculo(conteudoHtml, nomeArquivo):
    arquivo = open(nomeArquivo, "w", encoding="utf-8")
    arquivo.write(conteudoHtml)
    arquivo.close()
    print(f"\nO arquivo '{nomeArquivo}' foi criado.")

nome, email, telefone, endereco, resumo, formacoes, experiencias, foto, habilidades = coletarDados()
htmlGerado = gerarCurriculo(nome,email,telefone,endereco,resumo,formacoes,experiencias,foto,habilidades)
salvarCurriculo(htmlGerado, "curriculo.html")