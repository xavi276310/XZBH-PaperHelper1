import streamlit as st
from config import AUTHOR_IMAGE


def show_personal_page():
    st.markdown('<div class="eyebrow">关于作者</div>', unsafe_allow_html=True)
    st.title('你好，我是箫张跋扈')
    st.write('分享深度学习、模型模块与学术写作的实践经验。')
    st.markdown('我将常用的学术写作提示词整理成这个工具，希望帮你更快地组织问题、优化表达，把更多精力放在研究本身。')
    st.link_button('访问我的 B 站空间 ↗', 'https://space.bilibili.com/478113245', type='primary')
    st.divider()
    st.subheader('视频与学习资源')
    st.write('这里保留了两个模块融合实践视频入口，可结合自己的模型与研究任务参考学习。')
    first, second = st.columns(2)
    with first:
        with st.container(border=True):
            st.markdown('#### 模块融合实践 · 视频一')
            st.caption('原有视频资源')
            st.link_button('在 B 站观看 ↗', 'https://www.bilibili.com/video/BV1zg4y1C7oP/', use_container_width=True)
    with second:
        with st.container(border=True):
            st.markdown('#### 模块融合实践 · 视频二')
            st.caption('原有视频资源')
            st.link_button('在 B 站观看 ↗', 'https://www.bilibili.com/video/BV1Kw411G7Rw', use_container_width=True)
    st.divider()
    st.subheader('了解更多')
    st.write('欢迎通过下方图片了解更多课程与学习资料，也可以先从公开分享的视频开始。')
    if AUTHOR_IMAGE.is_file():
        image_col, _ = st.columns([2, 1])
        with image_col:
            st.image(str(AUTHOR_IMAGE), use_container_width=True, caption='课程与学习资料')
    else:
        st.info('更多内容可前往上方 B 站空间查看。')
