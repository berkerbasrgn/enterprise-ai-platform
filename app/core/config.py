from pydantic_settings import BaseSettings
from functools import lru_cache
import os
class Settings(BaseSettings):
    #uygulama
    app_name : str
    env : str = "dev"

    #database
    # postgresql baglanti adresi ilerde lazim olacak
    database_url : str = ""

    #Azure OpenAI
    # ilerde azure baglantisi icin
    azure_openai_key : str = ""
    azure_openai_key : str = ""
    azure_deployment_name : str = ""

    #logging
    # dev ile prod arasindaki fark burda
    log_level : str = "INFO"
    debug : bool = False

    class Config:
        env_file = os.getenv("ENV_FILE", ".env") #ENVM_FILE yoksa default .env
#least recently used cache 
# first call : fonksionu calistir sonucu sakla, sonraki calllarda saklanan sonucu ver tekrar calistirma
@lru_cache
def get_settings() -> Settings:
    return Settings()
# Settings() her olsutgunda .env dosyasini diskten okuyor
# 1000 istek gelirse 1000 kez disk okuma olur. lrucache ile bir kez okuyup hep ayni nesneyi kullaniyor.

settings = Settings()
