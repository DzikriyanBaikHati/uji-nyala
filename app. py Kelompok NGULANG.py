```python
import streamlit as st
import streamlit.components.v1 as components

# =========================
# KONFIGURASI HALAMAN
# =========================
st.set_page_config(
    page_title="ChemLearn Hub",
    page_icon="🧪",
    layout="centered"
)

# =========================
# SIDEBAR
# =========================
menu = st.sidebar.selectbox(
    "📚 Pilih Menu",
    ["Beranda", "Uji Nyala", "Titrasi Asam Basa"]
)

# =========================
# BERANDA
# =========================
if menu == "Beranda":

    st.title("🧪 ChemLearn Hub")
    st.subheader("Kelompok 2A - Kimia Dasar")

    st.image(
        "https://cdn.pixabay.com/photo/2020/03/17/03/32/laboratory-4936936_960_720.png",
        use_container_width=True
    )

    st.success("Selamat datang di aplikasi simulasi Kimia Interaktif")

    col1, col2, col3 = st.columns(3)

    col1.metric("🔥 Unsur Uji Nyala", "9")
    col2.metric("⚗️ Simulasi", "2")
    col3.metric("🧪 Kelompok", "2A")

    st.markdown("---")

    st.subheader("🤯 Fakta Kimia Menarik")

    fakta = [
        "🎆 Warna kembang api berasal dari logam yang dibakar.",
        "🌞 Natrium menghasilkan warna kuning terang seperti lampu jalan.",
        "🟢 Barium digunakan untuk membuat kembang api hijau.",
        "🔴 Stronsium digunakan untuk membuat kembang api merah.",
        "🟣 Sesium menghasilkan warna yang sangat langka dalam uji nyala.",
        "⚡ Tembaga menghasilkan warna hijau kebiruan yang indah."
    ]

    for f in fakta:
        st.info(f)

# =========================
# UJI NYALA
# =========================
elif menu == "Uji Nyala":

    st.header("🔥 Simulasi Uji Nyala Logam")

    logam = st.selectbox(
        "Pilih logam yang diuji:",
        [
            "Natrium (Na)",
            "Kalium (K)",
            "Kalsium (Ca)",
            "Tembaga (Cu)",
            "Stronsium (Sr)",
            "Barium (Ba)",
            "Litium (Li)",
            "Rubidium (Rb)",
            "Sesium (Cs)"
        ]
    )

    warna_teks = {
        "Natrium (Na)": "Kuning Terang 🟡",
        "Kalium (K)": "Ungu Muda 🟣",
        "Kalsium (Ca)": "Jingga 🟠",
        "Tembaga (Cu)": "Hijau Kebiruan 🔵",
        "Stronsium (Sr)": "Merah Menyala 🔴",
        "Barium (Ba)": "Hijau Apel 🟢",
        "Litium (Li)": "Merah Crimson ❤️",
        "Rubidium (Rb)": "Merah Ungu 💜",
        "Sesium (Cs)": "Biru Violet 💙"
    }

    warna_api = {
        "Natrium (Na)": "gold",
        "Kalium (K)": "violet",
        "Kalsium (Ca)": "orange",
        "Tembaga (Cu)": "turquoise",
        "Stronsium (Sr)": "red",
        "Barium (Ba)": "#7FFF00",
        "Litium (Li)": "#DC143C",
        "Rubidium (Rb)": "#C71585",
        "Sesium (Cs)": "#6A5ACD"
    }

    penjelasan = {
        "Natrium (Na)": "🔬 Elektron natrium memancarkan cahaya kuning pada sekitar 589 nm.",
        "Kalium (K)": "🔬 Kalium menghasilkan warna ungu muda pada sekitar 766 nm.",
        "Kalsium (Ca)": "🔬 Kalsium menghasilkan warna jingga sekitar 622 nm.",
        "Tembaga (Cu)": "🔬 Tembaga menghasilkan warna hijau kebiruan sekitar 510–520 nm.",
        "Stronsium (Sr)": "🔬 Stronsium menghasilkan warna merah terang sekitar 606–670 nm.",
        "Barium (Ba)": "🔬 Barium menghasilkan warna hijau apel yang digunakan pada kembang api.",
        "Litium (Li)": "🔬 Litium menghasilkan warna merah crimson yang khas.",
        "Rubidium (Rb)": "🔬 Rubidium menghasilkan warna merah keunguan.",
        "Sesium (Cs)": "🔬 Sesium menghasilkan warna biru-violet yang sangat langka."
    }

    fakta_logam = {
        "Natrium (Na)": "💡 Warna kuning natrium sangat kuat sehingga dapat menutupi warna unsur lain.",
        "Kalium (K)": "🍌 Kalium banyak ditemukan pada pisang.",
        "Kalsium (Ca)": "🦴 Kalsium merupakan penyusun utama tulang dan gigi.",
        "Tembaga (Cu)": "🔌 Tembaga digunakan sebagai penghantar listrik.",
        "Stronsium (Sr)": "🎇 Stronsium digunakan pada kembang api merah.",
        "Barium (Ba)": "🎆 Barium digunakan pada kembang api hijau.",
        "Litium (Li)": "🔋 Litium digunakan pada baterai smartphone.",
        "Rubidium (Rb)": "⏱ Rubidium digunakan dalam jam atom.",
        "Sesium (Cs)": "🛰 Sesium menjadi standar internasional pengukuran waktu."
    }

    if st.button("🔥 Mulai Uji Nyala"):

        st.success(f"Warna Nyala: {warna_teks[logam]}")
        st.info(penjelasan[logam])
        st.warning(fakta_logam[logam])

        st.markdown(f"""
| Parameter | Hasil |
|-----------|--------|
| Unsur | {logam} |
| Warna Nyala | {warna_teks[logam]} |
| Status | Berhasil ✅ |
| Metode | Flame Test 🔥 |
""")

        warna_nyala = warna_api[logam]

        components.html(
            f"""
            <div style="text-align:center;">
                <h2 style="color:{warna_nyala};">
                    Simulasi Api {logam}
                </h2>

                <div class="flame"></div>
            </div>

            <style>
            .flame {{
                margin:auto;
                width:100px;
                height:100px;
                border-radius:50%;
                background:radial-gradient(circle,
                {warna_nyala}, black);
                box-shadow:0 0 60px 30px {warna_nyala};
                animation:pulse 0.8s infinite alternate;
            }}

            @keyframes pulse {{
                from {{
                    transform:scale(1);
                    opacity:1;
                }}

                to {{
                    transform:scale(1.3);
                    opacity:0.6;
                }}
            }}
            </style>
            """,
            height=250
        )

        st.markdown("---")

        st.subheader("🏆 Ranking Warna Nyala")

        st.write("🥇 Sesium (Cs) — Biru Violet")
        st.write("🥈 Tembaga (Cu) — Hijau Kebiruan")
        st.write("🥉 Rubidium (Rb) — Merah Ungu")
        st.write("🏅 Barium (Ba) — Hijau Apel")

# =========================
# TITRASI ASAM BASA
# =========================
elif menu == "Titrasi Asam Basa":

    st.header("⚗️ Simulasi Titrasi Asam-Basa")

    st.markdown("""
### Rumus Dasar

Ma × Va = Mb × Vb

Keterangan:

- Ma = Konsentrasi Asam
- Va = Volume Asam
- Mb = Konsentrasi Basa
- Vb = Volume Basa
""")

    asam = st.selectbox(
        "Pilih Asam",
        ["HCl", "CH₃COOH"]
    )

    basa = st.selectbox(
        "Pilih Basa",
        ["NaOH", "KOH"]
    )

    Ma = st.number_input(
        "Konsentrasi Asam (mol/L)",
        0.1, 2.0, 1.0, 0.1
    )

    Va = st.slider(
        "Volume Asam (mL)",
        5, 50, 25
    )

    Mb = st.number_input(
        "Konsentrasi Basa (mol/L)",
        0.1, 2.0, 1.0, 0.1
    )

    Vb = (Ma * Va) / Mb

    st.success(
        f"🎯 Volume basa yang dibutuhkan = {Vb:.2f} mL"
    )

    volume_basa = st.slider(
        "Tambahkan Basa (mL)",
        0, 50, 0
    )

    delta = volume_basa - Vb

    if delta < 0:
        ph = 3 + (volume_basa / Vb) * 4
    elif delta == 0:
        ph = 7
    else:
        ph = 7 + min(delta * 0.5, 7)

    ph = round(ph, 1)

    st.metric("📊 pH Larutan", ph)

    if ph < 7:
        warna = "red"
        ket = "Larutan Bersifat Asam"
    elif ph == 7:
        warna = "blue"
        ket = "Titik Ekivalen (Netral)"
    else:
        warna = "green"
        ket = "Larutan Bersifat Basa"

    components.html(
        f"""
        <div style="text-align:center;">
            <div style="
                width:100px;
                height:100px;
                border-radius:50%;
                margin:auto;
                background:{warna};
                box-shadow:0 0 40px 20px {warna};
                animation:pulse 1s infinite alternate;
            ">
            </div>

            <h3 style="color:{warna};">
                {ket}
            </h3>
        </div>
        """,
        height=220
    )

    st.progress(min(int(ph / 14 * 100), 100))

    st.info(
        "💡 Pada titik ekivalen jumlah mol asam sama dengan jumlah mol basa sehingga larutan menjadi netral."
    )
```
