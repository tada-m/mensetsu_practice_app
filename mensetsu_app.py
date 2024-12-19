import streamlit as st
import time
# 質問と時間を定義
questions = [
    {"text": "志望動機を教えてください。", "time": 180},
    {"text": "自動車業界を志したきっかけは何ですか？", "time": 60},
    {"text": "自己紹介をお願いします。", "time": 60},
    {"text": "あなたがエンジニアを志したきっかけを教えてください。", "time": 60},
    {"text": "大学（または大学院）での研究内容について詳しく教えてください。", "time": 60},
    {"text": "研究でどういった点に苦労しましたか？", "time": 60},
    {"text": "受賞できたのはなぜだと思いますか？", "time": 60},
    {"text": "これまでに取り組んだプロジェクトの中で、特に印象に残っているものは何ですか？", "time": 60},
    {"text": "トヨタ自動車のインターンシップで学んだことは何ですか？", "time": 60},
    {"text": "コミュニケーション力が大事だと思った具体例は？", "time": 60},
    {"text": "学生時代に力を入れたことについて教えてください。", "time": 120},
    {"text": "トヨタ自動車を志望した理由を教えてください。", "time": 60},
    {"text": "自動車のコックピットシステムで重要だと思う技術要素は何だと思いますか？", "time": 60},
    {"text": "HMI（ヒューマンマシンインターフェース）について、どのような知識や経験がありますか？", "time": 60},
    {"text": "ソフトウェア開発において使用したことがあるプログラミング言語やツールについて教えてください。", "time": 60},
    {"text": "システムの最適化や改善を行った経験があれば教えてください。", "time": 60},
    {"text": "デザインと機能性を両立させるために、どのようなアプローチを取りますか？", "time": 60},
    {"text": "開発中に直面した困難な問題をどのように解決しましたか？", "time": 60},
    {"text": "システムトラブルが発生した場合、どのような手順で原因を特定し対応しますか？", "time": 60},
    {"text": "チームの意見が対立した際、どのように調整を行いますか？", "time": 60},
    {"text": "スケジュールが遅延している場合、どのようにリカバリーしますか？", "time": 60},
    {"text": "トヨタの「Kaizen（改善）」の理念に基づいて、どのように開発プロセスを効率化しますか？", "time": 60},
    {"text": "チームでの開発経験について教えてください。", "time": 60},
    {"text": "他部門との協力が必要な場合、どのように連携しますか？", "time": 60},
    {"text": "後輩や新しいメンバーに技術を教えた経験はありますか？", "time": 60},
    {"text": "他のメンバーがミスをしたとき、どのようにフォローしますか？", "time": 60},
    {"text": "チーム内でリーダーシップを発揮した経験を教えてください。", "time": 60},
    {"text": "5年後、10年後のキャリアプランについて教えてください。", "time": 60},
    {"text": "トヨタ自動車のコックピットシステムにどのような可能性を感じていますか？", "time": 60},
    {"text": "自動運転や電動化の進展によるコックピットシステムの変化について、どう対応していきたいですか？", "time": 60},
    {"text": "トヨタでどのような技術や製品を実現したいと思っていますか？", "time": 60},
    {"text": "最近の技術トレンド（例: AI、IoT）について、どのように学んでいますか？", "time": 60},
    {"text": "トヨタの「お客様第一」の理念について、あなたが開発において意識することは何ですか？", "time": 60},
    {"text": "ストレスの多い状況で、どのようにモチベーションを維持しますか？", "time": 60},
    {"text": "大量のデータを扱う際の課題と、その解決方法について教えてください。", "time": 60},
    {"text": "新しい技術や知識を習得する際に、どのような方法を取りますか？", "time": 60},
    {"text": "あなたの強みと弱みを、エンジニアとしての観点で教えてください。", "time": 60},
    {"text": "自動車のコックピットで新しい機能を追加するとしたら、どのようなアイデアを提案しますか？", "time": 60},
    {"text": "ユーザーからのフィードバックでHMIが使いにくいという指摘を受けた場合、どのように改善しますか？", "time": 60},
    {"text": "プロジェクトの納期が短縮された場合、どのタスクを優先し、どのタスクを後回しにしますか？", "time": 60},
    {"text": "AIを活用したドライバーの状態検知システムを開発する際の課題は何だと思いますか？", "time": 60},
    {"text": "自動運転時代のコックピット設計において、最も重要な要素は何だと考えますか？", "time": 60}
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