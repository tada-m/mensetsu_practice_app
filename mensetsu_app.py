import streamlit as st
import time
# 質問と時間を定義
questions = [
    {"text": "自己紹介をお願いします。", "time": 60},
    {"text": "自動車業界を志したきっかけは何ですか？", "time": 60},
    {"text": "あなたがエンジニアを志したきっかけを教えてください。", "time": 60},
    {"text": "大学（または大学院）での研究内容について詳しく教えてください。", "time": 60},
    {"text": "研究でどういった点に苦労しましたか？", "time": 60},
    {"text": "学生時代に力を入れたことについて教えてください。", "time": 120},
    {"text": "5年後、10年後のキャリアプランについて教えてください。", "time": 60}
]
# セッションステートの初期化
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
if "time_left" not in st.session_state:
    st.session_state.time_left = questions[st.session_state.current_question]["time"]
if "timer_running" not in st.session_state:
    st.session_state.timer_running = False
# タイマー更新関数
def update_timer():
    while st.session_state.timer_running and st.session_state.time_left > 0:
        time.sleep(1)
        st.session_state.time_left -= 1
        timer_placeholder.markdown(f"### 残り時間: {st.session_state.time_left}秒")
        if st.session_state.time_left == 0:
            st.session_state.timer_running = False
            break
# 質問の表示
st.write(f"### 質問: {questions[st.session_state.current_question]['text']}")
# タイマー表示エリア
timer_placeholder = st.empty()
timer_placeholder.markdown(f"### 残り時間: {st.session_state.time_left}秒")
# スタートボタン
if st.button("スタート"):
    if not st.session_state.timer_running:
        st.session_state.timer_running = True
        update_timer()
# 左右ボタンで質問を切り替え
col1, col2 = st.columns(2)
with col1:
    if st.button("← 戻る"):
        if st.session_state.current_question > 0:
            st.session_state.current_question -= 1
            st.session_state.time_left = questions[st.session_state.current_question]["time"]
            st.session_state.timer_running = False
            st.rerun()
with col2:
    if st.button("→ 次へ"):
        if st.session_state.current_question < len(questions) - 1:
            st.session_state.current_question += 1
            st.session_state.time_left = questions[st.session_state.current_question]["time"]
            st.session_state.timer_running = False
            st.rerun()
# 時間が切れた場合の通知
if st.session_state.time_left == 0:
    st.write("時間切れです！")
