# Script que resume os pontos chaves de um texto gerado pelo whisper a partir de um audio .mp3

Este projeto implementar um simples resumo gerado pelo ollama baseado em um texto que foi obtido a partir da transcrição do modelo whisper

## Pré-requisitos
- Python 3.8 ou superior
- Ollama instalado e em execução localmente
- Modelo LLaMA llama3.2:1b baixado no Ollama
- Whisper(o modelo pode ser baixado durante a execução do código caso não tenha instalado ainda)
- FFMPEG
## Instalação

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd <diretorio-do-projeto>
```

2. Instale as dependências necessárias:
```bash
pip install -r requirements.txt
```

3. Certifique-se de que o Ollama está em execução e os modelos necessários estão instalados:


4. Resumo do texto obtido para o audio do projeto:

* React é uma biblioteca desenvolvida e mantida pelo Facebook.
* Sintaxe: JSX (junção de JavaScript com XML).
* Funciona com um sistema de componentes, onde uma função retorna HTML ou componentes nativos.
* O React pode ser usado em aplicações web e aplicativos móveis.
* Existem frameworks como Next.js e Remix que são full-stack do React.
* O React é um sistema de componentes para gerar componentes nativos.


5. melhorias futuras
O projeto manda o texto completo para o ollama.
 funcionna bem deste modo, porém talvez uma forma de melhorar é transformar os textos em embeds e alimentar um banco FAISS a depender do caso de uso.
