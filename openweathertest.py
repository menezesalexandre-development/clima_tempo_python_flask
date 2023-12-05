import requests


def clima_tempo(nome_cidade):
    try:
        chave_api_pyowm = 'e4301b8a9bd9d49f970948fbd02f5b5f'

        url = f"https://api.openweathermap.org/data/2.5/weather?q={nome_cidade}&appid={chave_api_pyowm}"

        info_clima = dict()

        requisicao = requests.get(url)
        requisicao_dicionario = requisicao.json()
        info_clima['cidade'] = (requisicao_dicionario['name']).upper()
        info_clima['main'] = (requisicao_dicionario['weather'][0]['main']).upper()
        match info_clima['main']:
            case 'CLEAR':
                info_clima['desc_text'] = 'CÉU LIMPO'
                info_clima['desc_icon'] = 'ceu_limpo.png'
            case 'CLOUDS':
                info_clima['desc_text'] = 'PARCIALMENTE NUBLADO'
                info_clima['desc_icon'] = '/clima_icons/parcialmente_nublado.png'
            case 'DRIZZLE':
                info_clima['desc_text'] = 'CHUVA LEVE'
                info_clima['desc_icon'] = 'chuva_leve.png'
            case 'RAIN':
                info_clima['desc_text'] = 'CHUVA'
                info_clima['desc_icon'] = 'chuva.png'
            case 'THUNDERSTORM':
                info_clima['desc_text'] = 'TEMPESTADE'
                info_clima['desc_icon'] = 'tempestade.png'
            case 'SNOW':
                info_clima['desc_text'] = 'NEVE'
                info_clima['desc_icon'] = 'neve.png'
            case 'MIST':
                info_clima['desc_text'] = 'NÉVOA'
                info_clima['desc_icon'] = 'atmosphere.png'
            case 'SMOKE':
                info_clima['desc_text'] = 'NÉVOA'
                info_clima['desc_icon'] = 'atmosphere.png'
            case 'HAZE':
                info_clima['desc_text'] = 'NÉVOA'
                info_clima['desc_icon'] = 'atmosphere.png'
            case 'DUST':
                info_clima['desc_text'] = 'NÉVOA'
                info_clima['desc_icon'] = 'atmosphere.png'
            case 'FOG':
                info_clima['desc_text'] = 'NÉVOA'
                info_clima['desc_icon'] = 'atmosphere.png'
            case 'SAND':
                info_clima['desc_text'] = 'NÉVOA'
                info_clima['desc_icon'] = 'atmosphere.png'
            case 'ASH':
                info_clima['desc_text'] = 'NÉVOA'
                info_clima['desc_icon'] = 'atmosphere.png'
            case 'SQUALL':
                info_clima['desc_text'] = 'NÉVOA'
                info_clima['desc_icon'] = 'atmosphere.png'
            case 'TORNADO':
                info_clima['desc_text'] = 'TORNALDO'
                info_clima['desc_icon'] = 'atmosphere.png'
        info_clima['description'] = (requisicao_dicionario['weather'][0]['description']).upper()
        match info_clima['description']:
            case 'SCATTERED CLOUDS':
                info_clima['desc_text'] = 'NUBLADO'
                info_clima['desc_icon'] = 'nublado.png'
            case 'BROKEN CLOUDS':
                info_clima['desc_text'] = 'NUBLADO'
                info_clima['desc_icon'] = 'nublado.png'
            case 'OVERCAST CLOUDS':
                info_clima['desc_text'] = 'NUBLADO'
                info_clima['desc_icon'] = 'nublado.png'
            case 'FREEZING RAIN':
                info_clima['desc_text'] = 'CHUVA COM NEVE'
                info_clima['desc_icon'] = 'neve.png'
        info_clima['temperatura'] = f'{(requisicao_dicionario["main"]["temp"] - 273):.0f}°C'
        info_clima['umidade'] = f'{requisicao_dicionario["main"]["humidity"]}%'
        info_clima['visibilidade'] = f'{requisicao_dicionario["visibility"] / 1000}km'

        if requisicao_dicionario['cod'] == 200:
            return info_clima, requisicao_dicionario
        else:
            cidade_falha = 'Cidade não encontrada'
            return cidade_falha
    except:
        return 'Não foi possível executar o processo'


print(clima_tempo('Vitória da Conquista'))
