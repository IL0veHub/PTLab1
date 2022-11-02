from src.DataReaderXML import DataReaderXML
import pytest
from src.Types import DataType

class TestDataReaderXML:

    @pytest.fixture()
    def file_and_data_content(self) -> tuple[str, DataType]:
        text = "<students\n>" + \
                    "<student>\n" + \
                        "<name>Иванов</name>\n" + \
                        "<scores>\n" + \
                            "<object>\n" + \
                                "<object_name>Физика</object_name>\n" + \
                                "<object_value>76</object_value>\n" + \
                            "</object>\n" + \
                        "</scores>\n" + \
                    "</student>\n" + \
                "</students>\n"
        data = [{"name": "Иванов", "score": {"Физика":76}}]
        return text, data

    @pytest.fixture()
    def filepath_and_data(self,
                          file_and_data_content: tuple[str, DataType],
                          tmpdir) -> tuple[str, DataType]:
        p = tmpdir.mkdir("datadir").join("my_data.txt")
        p.write_text(file_and_data_content[0], encoding='utf-8')
        return str(p), file_and_data_content[1]

    def test_read(self, filepath_and_data: tuple[str, DataType]) -> None:
        file_content = DataReaderXML().read(filepath_and_data[0])
        assert file_content == filepath_and_data[1]
