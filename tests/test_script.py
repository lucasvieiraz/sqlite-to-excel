import subprocess
import os

def test_script_roda_e_gera_arquivos():
    # roda o script como se fosse no terminal
    result = subprocess.run(
        ["python", "planinhas_automatizadas.py"],
        capture_output=True,
        text=True
    )

    # verifica se rodou sem erro
    assert result.returncode == 0, f"Erro ao executar script: {result.stderr}"

    # verifica se os arquivos foram criados
    assert os.path.exists("relatorioAbastecimento09.xlsx")
    assert os.path.exists("veiculos_abastecidos.xlsx")
