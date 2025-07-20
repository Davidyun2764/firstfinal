import streamlit as st
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

def aes_decrypt(encrypted_b64, key_str):
    try:
        key = key_str.encode()
        data = base64.b64decode(encrypted_b64)
        iv = data[:16]
        ciphertext = data[16:]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        padded_plaintext = cipher.decrypt(ciphertext)
        plaintext = unpad(padded_plaintext, AES.block_size).decode()
        return plaintext, None
    except Exception as e:
        return None, f"복호화 오류: {str(e)}"

st.title("🔓 AES 복호화")
st.info("암호화에 사용한 키를 그대로 입력해야 복호화가 됩니다.")

if "show_go_encrypt" not in st.session_state:
    st.session_state.show_go_encrypt = False

key_input = st.text_input("복호화 키 입력 (16, 24, 32 바이트)", type="password")
key_bytes = len(key_input.encode())
key_chars = len(key_input)
st.caption(f"입력한 키: {key_chars}자 / {key_bytes}바이트")
valid_key_sizes = [16, 24, 32]

if key_input:
    if key_bytes not in valid_key_sizes:
        shortage = min([v for v in valid_key_sizes if v > key_bytes], default=None)
        if shortage:
            st.error(f"❗ 키가 {shortage - key_bytes} 바이트 부족합니다. (필요: {shortage}바이트)")
        else:
            st.error("❗ 키 길이가 맞지 않습니다. (16, 24, 32바이트 중 하나)")
        st.session_state.show_go_encrypt = False
    else:
        encrypted_input = st.text_area("복호화할 암호문(Base64)", value=st.session_state.get("encrypted_text", ""), height=150)
        if st.button("복호화 시작"):
            if not encrypted_input:
                st.error("암호문을 입력하세요.")
            else:
                result, error = aes_decrypt(encrypted_input, key_input)
                if error:
                    st.error(error)
                else:
                    st.success("✅ 복호화 성공!")
                    st.text_area("복호화된 평문", result, height=150)
                    st.session_state.show_go_encrypt = True
else:
    st.session_state.show_go_encrypt = False

# 복호화 성공 후 '다시 암호화하러 가기' 버튼 (입력값 초기화)
if st.session_state.get("show_go_encrypt", False):
    if st.button("🔁 다시 암호화하러 가기"):
        st.session_state.enc_key = ""
        st.session_state.encrypted_text = ""
        st.session_state.show_go_encrypt = False
        st.switch_page("pages/1_암호화하기.py")
