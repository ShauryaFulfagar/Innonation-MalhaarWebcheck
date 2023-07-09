import requests
from PIL import Image

base_url = 'https://api.qrcode-monkey.com/qr/custom'
api_key = 'YOUR_API_KEY'
project_file_path = '/path/to/project/files/logo.svg'

params = {
    'data': 'https://theindianschool.in',
    'config': {
        'body': 'frame3',
        'eye': 'eyeball1',
        'eyeBall': 'ball1',
        'gradientColor1': '#00aaff',
        'gradientColor2': '#0066ff',
        'gradientType': 'radial',
        'logo': 'file',
        'logoFile': project_file_path,
        'logoBackgroundColor': '#ffffff',
        'logoWidth': 30,
        'logoHeight': 30,
        'logoMargin': 10,
        'logoRadius': 5,
        'logoScale': 30,
        'quietZone': 10,
    }
}

response = requests.post(f'{base_url}/{api_key}', json=params)
data = response.json()

if data['success']:
    qr_code_url = data['data']['imageUrl']
    print('QR code generated successfully!')
    print('QR code URL:', qr_code_url)

    qr_code_image = Image.open(requests.get(qr_code_url, stream=True).raw)
    qr_code_image.save('qrcode.png', 'PNG')
    print('QR code saved as qrcode.png')
else:
    print('QR code generation failed.')
    print('Error message:', data['errorMessage'])
