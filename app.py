import streamlit as st

# 1. Инициализация на session_state
if 'animals' not in st.session_state:
    st.session_state.animals = []

st.title("🐾 Моята Галерия за Животни")

# 2. Секция за ДОБАВЯНЕ
st.header("Добави ново животно")
with st.form("addition_form", clear_on_submit=True):
    name = st.text_input("Име на животното")
    img_url = st.text_input("URL адрес на снимката")
    desc = st.text_area("Описание")
    
    submit_button = st.form_submit_button("Добави в галерията")
    
    if submit_button and name and img_url:
        new_animal = {
            "име": name,
            "картинка": img_url,
            "описание": desc
        }
        st.session_state.animals.append(new_animal)
        st.success(f"{name} беше добавено успешно!")
        st.rerun()

st.divider()

# 3. Секция за ПРЕМАХВАНЕ (от твоята снимка)
if st.session_state.animals:
    st.header("Премахни животно")
    
    # Създаваме списък само с имената за selectbox-а
    names = [a["име"] for a in st.session_state.animals]
    
    remove_name = st.selectbox("Избери животно за премахване", names)
    
    if st.button("Премахни"):
        for a in st.session_state.animals:
            if a["име"] == remove_name:
                st.session_state.animals.remove(a)
                st.rerun() # Опресняваме страницата веднага
                break
        st.success(f"{remove_name} е премахнато!")

st.divider()

# 4. Секция за ВИЗУАЛИЗАЦИЯ (от твоята снимка)
st.header("Галерия")
if st.session_state.animals:
    # Създаваме 3 колони за мрежови изглед
    cols = st.columns(3)
    
    for idx, animal in enumerate(st.session_state.animals):
        # Използваме оператора % (modulo), за да разпределяме животните в 3-те колони
        with cols[idx % 3]:
            st.subheader(animal["име"])
            st.image(animal["картинка"], use_container_width=True)
            st.write(animal["описание"])
else:
    st.info("Галерията е празна. Добавете животни!")
