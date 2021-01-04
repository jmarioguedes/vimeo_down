# Vimeo Downloader #

Script utilitário para baixar vídeos da plataforma [Vimeo](https://vimeo.com/).

Desenvolvido em Python 3.9 tirando proveito do AsyncIO, tem por objetivo fazer download dos segmentos de um 
vídeo da plataforma [Vimeo](https://vimeo.com/).

O projeto foi inspirado à partir deste: https://gist.github.com/mistic100/895f6d17b1e193334882a4c37d0d7748

Instruções para uso:

- Crie um arquivo INI local com a seguinte estrutura:

```ini
[GENERAL]
URL_MASTER=
DIR_TEMP=
```

- Crie um diretório, vazio, de trabalho e informe na chave `DIR_TEMP`

- Abra o site com o vídeo desejado, e com o DevTools acionado dê play no vídeo.

- Procure na aba "Network" a solicitação para `master.json` e informe a URL completa em `URL_MASTER`

![Aba Nerwork](.\assets\aba_network.png)

- Coloque o projeto em execução

- Ao fim do processo terão dois arquivos no diretório de trabalho:
    - @audio.mp4 - Com o áudio 
    - @video.mp4 - Com o vídeo 
    
- Utilize o software MKVTools para juntar os arquivos

👉🏻 Se gostou do que viu, me pague um cafezinho: Pix - jmarioguedes@gmail.com

- Seja feliz!
  