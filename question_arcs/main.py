from translator.question_translator import UminekoQuestionTranslator
from util.translate_progressive import translate_progressive

"""

For developers:
If you want to run this script by yourself, you need the following:
- Google Cloud Account and Project with the Cloud Translation API enabled
- A .env file located in the root of this project containing the following entry:
`GOOGLE_APPLICATION_CREDENTIALS=<path_to_google_app_credentials>`
- The 07th-Mod's original english script file, which is called `0.u`

Para desarrolladores:
Si quieres ejecutar este script por tí mismo, necesitas lo siguiente:
- Cuenta de Google Cloud y un Proyecto con la API de Cloud Translation activa
- Un fichero .env ubicado en la raíz de este proyecto conteniendo el siguiente registro:
`GOOGLE_APPLICATION_CREDENTIALS=<ruta_a_credenciales_de_aplicación_de_google>`
- El guión en inglés original de 07th-Mod, que se llama `0.u`

"""

if __name__ == '__main__':
    ut = UminekoQuestionTranslator()
    translate_progressive(ut, 500, 5, 30)