import streamlit as st
import control as ctrl

def main():
    st.title("Ferramenta SISO - Modelo Inicial")

    st.header("Configuração do Sistema")

    # Campos para entrada de zeros, polos e ganho
    zeros_input = st.text_input("Insira os zeros (separados por vírgulas):", "")
    poles_input = st.text_input("Insira os polos (separados por vírgulas):", "")
    gain_input = st.text_input("Insira o ganho:", "1")

    # Botão para criar a função de transferência
    if st.button("Criar Função de Transferência"):
        try:
            # Processando os inputs
            zeros = [float(z) for z in zeros_input.split(",") if z.strip()] if zeros_input else []
            poles = [float(p) for p in poles_input.split(",") if p.strip()] if poles_input else []
            gain = float(gain_input)

            # Criando a função de transferência
            system = ctrl.TransferFunction(ctrl.zpk(zeros, poles, gain))

            # Obtendo os coeficientes do numerador e denominador
            num, den = system.num[0][0], system.den[0][0]

            # Formatando a função de transferência em LaTeX
            num_str = " + ".join([f"{coef:.3g}s^{len(num) - i - 1}" if len(num) - i - 1 > 0 else f"{coef:.3g}"
                                  for i, coef in enumerate(num)])
            den_str = " + ".join([f"{coef:.3g}s^{len(den) - i - 1}" if len(den) - i - 1 > 0 else f"{coef:.3g}"
                                  for i, coef in enumerate(den)])

            tf_latex = f"\\frac{{{num_str}}}{{{den_str}}}"

            # Exibindo a função de transferência
            st.subheader("Função de Transferência")
            st.latex(tf_latex)

        except Exception as e:
            st.error(f"Erro ao processar os dados: {e}")

if __name__ == "__main__":
    main()
