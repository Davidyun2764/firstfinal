import streamlit as st
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import base64

def aes_encrypt(plaintext, key_str):
    key = key_str.encode()
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded = pad(plaintext.encode(), AES.block_size)
    ciphertext = cipher.encrypt(padded)
    return base64.b64encode(iv + ciphertext).decode()

st.title("🔐 AES 암호화")

st.markdown("""
#### 🔑 **암호화 키 안내**
- **암호화 키**란 암호화와 복호화에 모두 사용하는 ‘비밀번호’입니다.
- **키는 절대 노출되면 안 되며**, 꼭 기억해두어야 합니다.
- **키는 반드시 아래 조건을 만족해야 합니다.**
    - **16 바이트(128비트)**
    - **24 바이트(192비트)**
    - **32 바이트(256비트)**
- 영문/숫자/특수문자/한글 모두 가능하나, 한글이나 특수문자는 실제 바이트 수가 늘어날 수 있으니, 입력란 아래의 "바이트 수"를 참고하세요.
- 예시:  
    - 16바이트: `abcd1234abcd1234`  
    - 24바이트: `abcd1234abcd1234abcd5678`  
    - 32바이트: `abcd1234abcd1234abcd5678abcd5678`
""")

key_input = st.text_input("암호화 키 입력", type="password")
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
        st.session_state.show_go_decrypt = False
    else:
        plaintext = st.text_area("암호화할 평문 입력")
        if st.button("암호화 시작"):
            if not plaintext:
                st.error("평문을 입력하세요.")
            else:
                result = aes_encrypt(plaintext, key_input)
                st.session_state.encrypted_text = result
                st.success("✅ 암호화 성공!")
                st.text_area("암호문 (복사해서 복호화에 사용하세요)", result, height=150)
                st.session_state.show_go_decrypt = True
else:
    st.session_state.show_go_decrypt = False

# 암호화 성공 후 '복호화하러 가기' 버튼 표시 및 페이지 이동
if st.session_state.get("show_go_decrypt", False):
    if st.button("➡️ 복호화하러 가기"):
        st.switch_page("pages/2_복호화하기.py")
