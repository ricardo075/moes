import streamlit as st
import math

# Defina a senha
senha_correta = "ola"

# Solicita a senha ao usuário
senha_digitada = st.text_input("Digite a senha:", type="password")

# Verifica se a senha está correta e libera o acesso
if senha_digitada == senha_correta:
    st.write("Senha correta. Você pode acessar o site.")
    # Restante do código do seu site
    def calcular_raizes_quadraticas(a, b, c):
        # Calculando o discriminante
        delta = b ** 2 - 4 * a * c

        # Verificando se o discriminante é positivo, negativo ou zero
        if delta > 0:
            raiz_delta = math.sqrt(delta)
            x1 = (-b - raiz_delta) / (2 * a)
            x2 = (-b + raiz_delta) / (2 * a)
            st.write("O discriminante é positivo, portanto, existem duas raízes reais distintas:")
            st.write("x1 =", x1)
            st.write("x2 =", x2)
        elif delta == 0:
            x1 = -b / (2 * a)
            st.write("O discriminante é zero, portanto, existe uma raiz real:")
            st.write("x1 =", x1)
        else:
            st.write("O discriminante é negativo, portanto, as raízes são números complexos.")


    # Interface do usuário
    st.title("Calculadora de raízes quadráticas")
    a = st.number_input("Insira o valor de a:", value=1.0)
    b = st.number_input("Insira o valor de b:", value=0.0)
    c = st.number_input("Insira o valor de c:", value=0.0)

    if st.button("Calcular raízes"):
        calcular_raizes_quadraticas(a, b, c)
else:
    st.write("Senha incorreta. Acesso negado.")








