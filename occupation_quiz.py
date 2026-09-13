import time
import streamlit as st

st.title("⏱️ เกมเติมศัพท์จับเวลา 👨‍🏫👩‍🚒👨‍✈️👨‍⚕️👮‍♂️")

if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""
if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""
if "ans3_val" not in st.session_state:
    st.session_state.ans3_val = ""
if "ans4_val" not in st.session_state:
    st.session_state.ans4_val = ""
if "ans5_val" not in st.session_state:
    st.session_state.ans5_val = ""



def reset_game():
    st.session_state.ans1_val = ""
    st.session_state.ans2_val = ""
    st.session_state.ans3_val = ""
    st.session_state.ans4_val = ""
    st.session_state.ans5_val = ""
    st.session_state.start = time.time()
    st.session_state.is_ended = False


@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2, ans3, ans4, ans5):
    st.balloons()
    score = 0

    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()
    u_ans3 = ans3.strip().lower()
    u_ans4 = ans4.strip().lower()
    u_ans5 = ans5.strip().lower()

    if u_ans1 == "police":
        st.success("✅ ข้อ 1: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 1: ยังไม่ถูกต้อง (คุณตอบ '{u_ans1}')")
        

    if u_ans2 == "teacher":
        st.success("✅ ข้อ 2: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 2: ยังไม่ถูกต้อง (คุณตอบ '{u_ans2}')")
        
        
    if u_ans3 == "doctor":
        st.success("✅ ข้อ 3: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 3: ยังไม่ถูกต้อง (คุณตอบ '{u_ans3}')")
                                             
    
    if u_ans4 == "firefighter":
        st.success("✅ ข้อ 4: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 4: ยังไม่ถูกต้อง (คุณตอบ '{u_ans4}')")
   
  
    if u_ans5 == "pilot":
        st.success("✅ ข้อ 5: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 5: ยังไม่ถูกต้อง (คุณตอบ '{u_ans5}')")
    
    st.info(f"🏆 ได้คะแนนรวม: {score} คะแนน")

    if score == 1:
        st.success("กาก 🐓")
    else:
        st.error("💀 You lose!")
        
    if score == 2:
        st.success("ไปฝึกมาใหม่ 🥀")
    else:
        st.error("💀 You lose!")
        
    if score == 3:
        st.success("คนทั่วไป 👍")
    else:
        st.error("💀 You lose!")

    if score == 4:
        st.success("โหด 🤑")
    else:
        st.error("💀 You lose!")

    if score == 5:
        st.success("bro is larping 🔥🔥")
    else:
        st.error("💀 You lose!")
        

st.button("🎮 เริ่มเล่นเกม", on_click=reset_game)

if "start" in st.session_state and not st.session_state.get("is_ended", False):
    time_left = int(60 - (time.time() - st.session_state.start))

    if time_left > 0:
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()

st.divider()

ans1 = st.text_input(
    "ข้อ 1: The `p _ _ i c _` catch criminals.",
    value=st.session_state.ans1_val,
)
ans2 = st.text_input(
    "ข้อ 2: The `_ _ a c h e r` teaches mathematics.",
    value=st.session_state.ans2_val,
)
ans3 = st.text_input(
    "ข้อ 3: The `d _ c _ _ r` treats cancer patients with specialized medical care.",
    value=st.session_state.ans3_val,
)
ans4 = st.text_input(
    "ข้อ 4: The `f _ r e _ _ g h t e r` puts out fires.",
    value=st.session_state.ans4_val,
)
ans5 = st.text_input(
    "ข้อ 5: The `p _ l _ t` flies a plane to Paris.",
    value=st.session_state.ans5_val,
)
    

st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
st.session_state.ans3_val = ans3
st.session_state.ans4_val = ans4
st.session_state.ans5_val = ans5

if "start" in st.session_state and not st.session_state.get("is_ended", False):
    if st.button("📥 ส่งคำตอบ"):
        st.session_state.is_ended = True
        st.rerun()

    time.sleep(1)
    st.rerun()

if st.session_state.get("is_ended", False):
    show_result_dialog(ans1, ans2, ans3, ans4, ans5)
