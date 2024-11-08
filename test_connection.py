import requests

# URL y headers de la solicitud
url = "https://api2.acb.com/api/v1/openapilive/Weeks/current?idCompetition=1&idEdition=89"
games = "https://api2.acb.com/api/v1/openapilive/Matches/matchesbyweeklite"
boxscore = "https://api2.acb.com/api/v1/openapilive/Boxscore/playermatchstatistics?idMatch="
pbp = "https://api2.acb.com/api/v1/openapilive/PlayByPlay/matchevents?idMatch="

headers = {
    "Authorization": "H4sIAAAAAAAAA32Ry3aqMBSG36iLi7qOw4oFk9PEQyohZEYilkCirIMF5OkbOmiVQUdZ+/bv798pbrAUkVR7BUEyAhcr0IIzWcoArEDdMBrA9VNxg5BPiQqp1wDGnEGTp/009MIZD4sd0dIsSxFMw7ATUaL2ulWxN7jZGV2poTegehuvrzKiTp7iRniL7zxhoZuzTZl5uhPKTTkD055Q+qTkkR6Pka4y9qNDTDjyu/hg6zxdVnkajq+UazmZ0Bstz7gT5j5HGhmtx4MPa9s/34dyxvUj41LL22OdMOxkqdXxSZN5d9r10BwNDS2v5Vh/zPg8ntD6W9OhwzHVvfDnPU033ZFHL495uinlmTTcsv/q5Yshmc+2GdNB8fXWs32wK3a4Ej7UMx8JT13LBy3LvUdsNXDDjf2P2X3YW6+EgQZUlwEf6gXeIgdvk4W9my52z2pfAReNcY8q1KPte4+CXtn/cub9p/jJef7j/Xvf/j150Sag6C1ctS41qVe3p6Fml5U4gf/xdecli8sn/TA0Eb8CAAA="
}

# Realizar la solicitud GET
pbp = pbp + "103836"
response = requests.get(pbp, headers=headers)

# Verificar el código de respuesta
if response.status_code == 200:
    # Mostrar el contenido de la respuesta en formato JSON
    data = response.json()
    #print(data)
    if type(data) == list: 
        # for dic in data: 
        #     print(dic.keys())
        print(f"Hi ha {len(data)} elements a dins de data")
        with open(r'./pbp.txt', 'w') as doc:
            for item in data:
                doc.write("%s\n" % item)
            print("Fet")
    else:
        print(data)
else:
    print(f"Error: {response.status_code}")
    print(response.text)
