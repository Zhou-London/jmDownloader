import jmcomic


class jmcomic_service:
    def fetch(self, id: str):
        option = jmcomic.create_option_by_file("src/config/jm_config.yml")
        jmcomic.download_album(jm_album_id=id, option=option)


jmcomic_agent = jmcomic_service()
