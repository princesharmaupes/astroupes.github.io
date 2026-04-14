---
layout: home
title: Activities
---

# 🚀 Recent Activities

---

## 🎓 February 2026: National Workshop on Data Science in Astronomy (Success Story)

The **National Workshop on Data Science in Astronomy (NWDSA)** was successfully organized at **UPES, Dehradun** from **24-26 February 2026** with academic support from IUCAA and active participation from students, faculty, and early-career researchers.

The workshop blended keynote lectures, guided hands-on labs, and participant-led project/presentation sessions. Participants worked with real astronomical datasets and strengthened practical skills in data handling, visualization, and time-series analysis.

**Workshop impact and outcomes:**
- Strong interdisciplinary participation from physics, astronomy, mathematics, and computer science backgrounds.
- Successful completion of hands-on sessions using Python-based scientific tools.
- Active poster and project discussions that encouraged collaborative learning.
- Valuable research networking between participants, speakers, and organizing faculty.

<div style="display: flex; gap: 24px; align-items: flex-start; margin-top: 24px; flex-wrap: wrap;">
  <div style="flex: 0 0 30%; min-width: 250px; max-width: 360px; background: #f7f7f7; padding: 18px 12px; border-radius: 8px; font-size: 1em; box-sizing: border-box; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
    <strong>Event:</strong> National Workshop on Data Science in Astronomy<br>
    <strong>Dates:</strong> 24th - 26th February 2026<br>
    <strong>Venue:</strong> UPES, Dehradun<br>
    <strong>Format:</strong> Talks + Hands-on + Project/Poster sessions<br>
    <strong>Status:</strong> Successfully completed
  </div>
  <div style="flex: 1 1 520px; max-width: 700px;">
    <div style="width: 100%; max-width: 620px; height: 380px; margin-left: auto; margin-right: auto; position: relative;">
      <div id="nwdsaSlideshow" style="position: relative; width: 100%; height: 100%; overflow: hidden; border-radius: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); background: #f0f3f7;">
        <img src="assests/images/NWDSA/DSCF0007.JPG" alt="NWDSA Workshop Glimpse" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: contain; background: #0b1220; display: block; transition: opacity 0.8s ease-in-out; opacity: 1;" id="nwdsaSlideA">
        <img src="assests/images/NWDSA/DSCF0333.JPG" alt="NWDSA Workshop Glimpse" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: contain; background: #0b1220; display: block; transition: opacity 0.8s ease-in-out; opacity: 0;" id="nwdsaSlideB">
        <button onclick="prevNwdsaSlide()" aria-label="Previous Slide" style="position: absolute; top: 50%; left: 10px; transform: translateY(-50%); background: rgba(0,0,0,0.5); color: #fff; border: none; border-radius: 50%; width: 34px; height: 34px; cursor: pointer;">&#8592;</button>
        <button onclick="nextNwdsaSlide()" aria-label="Next Slide" style="position: absolute; top: 50%; right: 10px; transform: translateY(-50%); background: rgba(0,0,0,0.5); color: #fff; border: none; border-radius: 50%; width: 34px; height: 34px; cursor: pointer;">&#8594;</button>
      </div>
      <p style="text-align: center; font-size: 0.95em; color: #555; margin-top: 8px;">Highlights from the National Workshop on Data Science in Astronomy (NWDSA 2026).</p>
    </div>
  </div>
</div>

<script>
  const nwdsaImages = [
    "assests/images/NWDSA/DSCF0007.JPG",
    "assests/images/NWDSA/DSCF0333.JPG",
    "assests/images/NWDSA/DSCF0590.JPG",
    "assests/images/NWDSA/DSCF0643.JPG",
    "assests/images/NWDSA/DSCF0704.JPG",
    "assests/images/NWDSA/DSCF0963.JPG",
    "assests/images/NWDSA/DSCF1124.JPG",
    "assests/images/NWDSA/DSCF1203.JPG",
    "assests/images/NWDSA/DSCF1240.JPG",
    "assests/images/NWDSA/DSCF1397.JPG",
    "assests/images/NWDSA/DSCF1432.JPG",
    "assests/images/NWDSA/DSCF1451.JPG",
    "assests/images/NWDSA/DSCF1457.JPG",
    "assests/images/NWDSA/DSCF9589.JPG",
    "assests/images/NWDSA/DSCF9620.JPG",
    "assests/images/NWDSA/DSCF9680.JPG",
    "assests/images/NWDSA/DSCF9918.JPG",
    "assests/images/NWDSA/DSCF9922.JPG",
    "assests/images/NWDSA/DSCF9982.JPG",
    "assests/images/NWDSA/DSCF9994.JPG",
    "assests/images/NWDSA/UPES-1.JPG",
    "assests/images/NWDSA/UPES-2.JPG"
  ];

  let nwdsaIndex = 0;
  let nwdsaActiveLayer = 'A';

  function preloadImages(imageList) {
    imageList.forEach((src) => {
      const img = new Image();
      img.src = src;
    });
  }

  function showNwdsaSlide(idx) {
    const slideA = document.getElementById('nwdsaSlideA');
    const slideB = document.getElementById('nwdsaSlideB');
    if (!slideA || !slideB) return;

    const current = nwdsaActiveLayer === 'A' ? slideA : slideB;
    const next = nwdsaActiveLayer === 'A' ? slideB : slideA;
    next.src = nwdsaImages[idx];

    requestAnimationFrame(() => {
      next.style.opacity = 1;
      current.style.opacity = 0;
      nwdsaActiveLayer = nwdsaActiveLayer === 'A' ? 'B' : 'A';
    });
  }

  function prevNwdsaSlide() {
    nwdsaIndex = (nwdsaIndex - 1 + nwdsaImages.length) % nwdsaImages.length;
    showNwdsaSlide(nwdsaIndex);
  }

  function nextNwdsaSlide() {
    nwdsaIndex = (nwdsaIndex + 1) % nwdsaImages.length;
    showNwdsaSlide(nwdsaIndex);
  }

  document.addEventListener('DOMContentLoaded', () => {
    preloadImages(nwdsaImages);
  });

  setInterval(() => {
    nextNwdsaSlide();
  }, 3800);
</script>

<br>

---

## 🌙 December 2025: Night Sky Observation (NSO) Event

The **Night Sky Observation (NSO)** event was conducted on **2nd December 2025**, offering students and enthusiasts a direct observational astronomy experience under the evening sky.

Participants observed key celestial targets through telescope-guided sessions and received live explanations on sky navigation, star identification, and observation practices. The event successfully connected classroom astronomy with real-sky exploration.

**Event details:**
- **Date:** 2nd December 2025
- **Format:** Guided night observation + faculty interaction
- **Focus:** Telescope orientation, constellation tracking, and practical sky awareness
- **Outcome:** Strong student engagement and hands-on observational confidence

<div style="width: 100%; max-width: 760px; margin: 20px auto 0; position: relative;">
  <div id="nsoSlideshow" style="position: relative; width: 100%; height: 420px; overflow: hidden; border-radius: 10px; background: #0b1220; box-shadow: 0 2px 8px rgba(0,0,0,0.12);">
    <img src="assests/images/NSO/DSCF8471.jpg" alt="Night Sky Observation event glimpse" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: contain; transition: opacity 0.8s ease-in-out; opacity: 1;" id="nsoSlideA">
    <img src="assests/images/NSO/DSCF8474.jpg" alt="Night Sky Observation event glimpse" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: contain; transition: opacity 0.8s ease-in-out; opacity: 0;" id="nsoSlideB">
    <button onclick="prevNsoSlide()" aria-label="Previous NSO slide" style="position: absolute; top: 50%; left: 10px; transform: translateY(-50%); background: rgba(0,0,0,0.5); color: #fff; border: none; border-radius: 50%; width: 34px; height: 34px; cursor: pointer;">&#8592;</button>
    <button onclick="nextNsoSlide()" aria-label="Next NSO slide" style="position: absolute; top: 50%; right: 10px; transform: translateY(-50%); background: rgba(0,0,0,0.5); color: #fff; border: none; border-radius: 50%; width: 34px; height: 34px; cursor: pointer;">&#8594;</button>
  </div>
  <p style="text-align: center; font-size: 0.95em; color: #555; margin-top: 8px;">Moments from the Night Sky Observation event at UPES.</p>
</div>

<script>
  const nsoImages = [
    "assests/images/NSO/DSCF8471.jpg",
    "assests/images/NSO/DSCF8474.jpg",
    "assests/images/NSO/DSCF8484.jpg",
    "assests/images/NSO/DSCF8512.jpg",
    "assests/images/NSO/DSCF8525.jpg",
    "assests/images/NSO/DSCF8584.JPG",
    "assests/images/NSO/DSCF8585.JPG",
    "assests/images/NSO/DSCF8605.JPG",
    "assests/images/NSO/DSCF8615.JPG",
    "assests/images/NSO/DSCF8625.JPG",
    "assests/images/NSO/DSCF8658.jpg",
    "assests/images/NSO/DSCF8659.jpg",
    "assests/images/NSO/DSCF8697.jpg",
    "assests/images/NSO/DSCF8705.jpg",
    "assests/images/NSO/DSCF8723.jpg"
  ];

  let nsoIndex = 0;
  let nsoActiveLayer = 'A';

  function showNsoSlide(idx) {
    const slideA = document.getElementById('nsoSlideA');
    const slideB = document.getElementById('nsoSlideB');
    if (!slideA || !slideB) return;

    const current = nsoActiveLayer === 'A' ? slideA : slideB;
    const next = nsoActiveLayer === 'A' ? slideB : slideA;
    next.src = nsoImages[idx];

    requestAnimationFrame(() => {
      next.style.opacity = 1;
      current.style.opacity = 0;
      nsoActiveLayer = nsoActiveLayer === 'A' ? 'B' : 'A';
    });
  }

  function prevNsoSlide() {
    nsoIndex = (nsoIndex - 1 + nsoImages.length) % nsoImages.length;
    showNsoSlide(nsoIndex);
  }

  function nextNsoSlide() {
    nsoIndex = (nsoIndex + 1) % nsoImages.length;
    showNsoSlide(nsoIndex);
  }

  document.addEventListener('DOMContentLoaded', () => {
    preloadImages(nsoImages);
  });

  setInterval(() => {
    nextNsoSlide();
  }, 4000);
</script>

<br>

---

## 🛰️ August 2025: National Space Day 2025 Event

On the occasion of the 2nd National Space Day, **Prof. Varun Sheel** (Head, Planetary Science Division, PRL) delivered a special talk.

<div style="display: flex; gap: 24px; align-items: flex-start; margin-top: 24px;">
  <div style="flex: 0 0 30%; max-width: 30%; background: #f7f7f7; padding: 18px 12px; border-radius: 8px; font-size: 1em; box-sizing: border-box; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
    <strong>Date:</strong> <span style="color: #2a7ae2;">22nd August 2025</span><br>
    <strong>Time:</strong> 3:00 – 4:00 pm<br>
    <strong>Venue:</strong> Buzz-II (Room #9104)
  </div>
  <div style="flex: 0 0 70%; max-width: 70%;">
    <div style="width: 480px; height: 320px; margin-left: auto; margin-right: auto; position: relative;">
      <div id="varunTalkSlideshow" style="position: relative; width: 100%; height: 100%; overflow: hidden; border-radius: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.08);">
        <img src="assests/images/varun_talk/slide1.jpg" alt="Varun Talk Slide 1" style="width: 100%; height: 100%; object-fit: cover; display: block; transition: opacity 0.6s;" id="varunTalkSlide">
        <button onclick="prevVarunTalkSlide()" aria-label="Previous Slide" style="position: absolute; top: 50%; left: 10px; transform: translateY(-50%); background: rgba(0,0,0,0.5); color: #fff; border: none; border-radius: 50%; width: 32px; height: 32px; cursor: pointer;">&#8592;</button>
        <button onclick="nextVarunTalkSlide()" aria-label="Next Slide" style="position: absolute; top: 50%; right: 10px; transform: translateY(-50%); background: rgba(0,0,0,0.5); color: #fff; border: none; border-radius: 50%; width: 32px; height: 32px; cursor: pointer;">&#8594;</button>
      </div>
      <p style="text-align: center; font-size: 0.95em; color: #555; margin-top: 8px;">Swipe through moments from Prof. Varun Sheel's talk.</p>
    </div>
  </div>
</div>

<script>
  const varunTalkImages = [
    "assests/images/varun_talk/slide1.jpg",
    "assests/images/varun_talk/slide2.jpg",
    "assests/images/varun_talk/slide3.jpg",
    "assests/images/varun_talk/slide4.jpg"
  ];
  let varunTalkIndex = 0;
  let varunTalkSlide = null;

  function showVarunTalkSlide(idx) {
    if (!varunTalkSlide) varunTalkSlide = document.getElementById('varunTalkSlide');
    if (varunTalkSlide) {
      varunTalkSlide.style.opacity = 0;
      setTimeout(() => {
        varunTalkSlide.src = varunTalkImages[idx];
        varunTalkSlide.style.opacity = 1;
      }, 300);
    }
  }
  function prevVarunTalkSlide() {
    varunTalkIndex = (varunTalkIndex - 1 + varunTalkImages.length) % varunTalkImages.length;
    showVarunTalkSlide(varunTalkIndex);
  }
  function nextVarunTalkSlide() {
    varunTalkIndex = (varunTalkIndex + 1) % varunTalkImages.length;
    showVarunTalkSlide(varunTalkIndex);
  }
  document.addEventListener('DOMContentLoaded', () => {
    varunTalkSlide = document.getElementById('varunTalkSlide');
    varunTalkSlide.style.opacity = 1;
  });
  setInterval(() => {
    nextVarunTalkSlide();
  }, 4000);
</script>

<br>

---

## 🌄 April 2025: Student Visit to ARIES, Nainital

A group of undergraduate students undertook a memorable academic expedition to the **Aryabhatta Research Institute of Observational Sciences (ARIES)**, Nainital.

This educational visit provided a rare opportunity for students to interact directly with professional astronomers, scientists, and engineers, gaining firsthand insights into India's leading research programs in observational astronomy. The visit featured informative sessions on exo-planet detection, Solar dynamics, observational strategies, and ongoing national missions.

**Highlights of the trip:**
- **Devasthal Optical Telescope (DOT)** – India’s largest optical telescope (Largest in Asia)
- **Devasthal Fast Optical Telescope (DFOT)** – rapid follow-up observations
- **International Liquid Mirror Telescope (ILMT)** – first liquid mirror telescope dedicated to astronomy

The exposure to operational observatories and interactions with the scientific community at ARIES made this visit a milestone in their academic journey.

**A glance into the visit:**

<div style="display: flex; flex-wrap: wrap; gap: 15px; margin-top: 10px; justify-content: center;">
  <a href="assests/images/ARIES_TRIP_2025/WhatsApp Image 2025-04-10 at 16.08.42_49bae8cc.jpg" target="_blank">
    <img src="assests/images/ARIES_TRIP_2025/WhatsApp Image 2025-04-10 at 16.08.42_49bae8cc.jpg" alt="ARIES Trip 1" style="width: auto; height: 200px; object-fit: cover; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.08);">
  </a>
  <a href="assests/images/ARIES_TRIP_2025/IMG-20250413-WA0017.jpg" target="_blank">
    <img src="assests/images/ARIES_TRIP_2025/IMG-20250413-WA0017.jpg" alt="ARIES Trip 2" style="width: auto; height: 200px; object-fit: cover; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.08);">
  </a>
  <a href="assests/images/ARIES_TRIP_2025/IMG-20250413-WA0051.jpg" target="_blank">
    <img src="assests/images/ARIES_TRIP_2025/IMG-20250413-WA0051.jpg" alt="ARIES Trip 3" style="width: auto; height: 200px; object-fit: cover; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.08);">
  </a>
  <a href="assests/images/ARIES_TRIP_2025/WhatsApp Image 2025-04-10 at 15.30.12_ad61e5fc.jpg" target="_blank">
    <img src="assests/images/ARIES_TRIP_2025/WhatsApp Image 2025-04-10 at 15.30.12_ad61e5fc.jpg" alt="ARIES Trip 4" style="width: auto; height: 200px; object-fit: cover; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.08);">
  </a>
  <a href="assests/images/ARIES_TRIP_2025/WhatsApp Image 2025-04-10 at 16.08.56_b245eda9.jpg" target="_blank">
    <img src="assests/images/ARIES_TRIP_2025/WhatsApp Image 2025-04-10 at 16.08.56_b245eda9.jpg" alt="ARIES Trip 5" style="width: auto; height: 200px; object-fit: cover; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.08);">
  </a>
</div>

---

## 🌟 March 2025: Weekly Lecture Series on Astrophysics

The *Weekly Lecture Series on Astrophysics* is an ongoing initiative introducing students to astronomy and astrophysics. Open to all, the series explores stellar evolution, black holes, and modern observational techniques, sparking curiosity and interdisciplinary engagement.

<div style="display: flex; gap: 24px; align-items: flex-start; margin-top: 24px;">
  <div style="flex: 0 0 30%; max-width: 30%; background: #f7f7f7; padding: 18px 12px; border-radius: 8px; font-size: 1em; box-sizing: border-box; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
    <strong>Lecture Series Speakers:</strong>
    <ul style="margin-top: 10px; padding-left: 18px;">
      <li><strong>Dr. Balendra P. Singh</strong></li>
      <li><strong>Dr. Nitesh Kumar</strong></li>
      <li><strong>Dr. Prince Sharma</strong></li>
      <li><strong>Dr. Arka Chatterjee</strong></li>
      <li><strong>Dr. Suvankar R. Chowdhury</strong></li>
      <li><strong>Dr. Raju RoyChowdhury</strong></li>
    </ul>
  </div>
  <div style="flex: 0 0 70%; max-width: 70%;">
    <div style="width: 480px; height: 640px; margin-left: auto; margin-right: auto; position: relative;">
      <div id="lectureSeriesSlideshow" style="position: relative; width: 100%; height: 100%; overflow: hidden; border-radius: 10px; background: #eee; box-shadow: 0 2px 8px rgba(0,0,0,0.08);">
        <img src="assests/images/LECTURE_SERIES_2025/nitesh_talk_poster.jpg" alt="Lecture Series Poster 2" style="width: 100%; height: 100%; object-fit: contain; display: block; transition: opacity 0.6s;" id="lectureSeriesSlide">
        <button onclick="prevLectureSeriesSlide()" aria-label="Previous Slide" style="position: absolute; top: 50%; left: 10px; transform: translateY(-50%); background: rgba(0,0,0,0.5); color: #fff; border: none; border-radius: 50%; width: 32px; height: 32px; cursor: pointer;">&#8592;</button>
        <button onclick="nextLectureSeriesSlide()" aria-label="Next Slide" style="position: absolute; top: 50%; right: 10px; transform: translateY(-50%); background: rgba(0,0,0,0.5); color: #fff; border: none; border-radius: 50%; width: 32px; height: 32px; cursor: pointer;">&#8594;</button>
      </div>
      <div id="lectureSeriesCaption" style="text-align: center; font-size: 0.95em; color: #555; margin-top: 8px;">
        Lecture 2 by Dr. Nitesh Kumar on "<em>Measuring the Universe: The Cosmic Ladder</em>"
      </div>
    </div>
    <script>
      const lectureSeriesImages = [
        {
          src: "assests/images/LECTURE_SERIES_2025/nitesh_talk_poster.jpg",
          caption: 'Lecture 2 by Dr. Nitesh Kumar on "<em>Measuring the Universe: The Cosmic Ladder</em>"'
        },
        {
          src: "assests/images/LECTURE_SERIES_2025/prince_talk.jpeg",
          caption: 'Lecture 3 by Dr. Prince Sharma on "<em>Life Cycle of Stars</em>"'
        },
        {
          src: "assests/images/LECTURE_SERIES_2025/suvankar.jpg",
          caption: 'Lecture 5 by Dr. Suvankar R. Chowdhury on "<em>Inward Bound: From Rutherford to Large Hadron Collider</em>"'
        },
        {
          src: "assests/images/LECTURE_SERIES_2025/raju_talk.png",
          caption: 'Lecture 6 by Dr. Raju Roychowdhury on "<em>The Einstein Window: A Voyage in Spacetime</em>"'
        }
      ];
      let lectureSeriesIndex = 0;
      let lectureSeriesSlide = null;
      let lectureSeriesCaption = null;

      function showLectureSeriesSlide(idx) {
        if (!lectureSeriesSlide) lectureSeriesSlide = document.getElementById('lectureSeriesSlide');
        if (!lectureSeriesCaption) lectureSeriesCaption = document.getElementById('lectureSeriesCaption');
        if (lectureSeriesSlide && lectureSeriesCaption) {
          lectureSeriesSlide.style.opacity = 0;
          setTimeout(() => {
            lectureSeriesSlide.src = lectureSeriesImages[idx].src;
            lectureSeriesCaption.innerHTML = lectureSeriesImages[idx].caption;
            lectureSeriesSlide.style.opacity = 1;
          }, 300);
        }
      }
      function prevLectureSeriesSlide() {
        lectureSeriesIndex = (lectureSeriesIndex - 1 + lectureSeriesImages.length) % lectureSeriesImages.length;
        showLectureSeriesSlide(lectureSeriesIndex);
      }
      function nextLectureSeriesSlide() {
        lectureSeriesIndex = (lectureSeriesIndex + 1) % lectureSeriesImages.length;
        showLectureSeriesSlide(lectureSeriesIndex);
      }
      document.addEventListener('DOMContentLoaded', () => {
        lectureSeriesSlide = document.getElementById('lectureSeriesSlide');
        lectureSeriesCaption = document.getElementById('lectureSeriesCaption');
        lectureSeriesSlide.style.opacity = 1;
      });
      setInterval(() => {
        nextLectureSeriesSlide();
      }, 4000);
    </script>
  </div>
</div>

<br>

---

## 🔭 February 2025: Sky-Gazing Event with In-House 12-inch Telescope

A sky-gazing session was organized using the department’s in-house 12-inch reflector telescope, giving students a rare opportunity to explore the skies from campus.

The event featured a guided solar observation session, where students safely viewed the Sun through a solar filter, observing sunspots and experiencing the dynamic nature of our nearest star. Faculty members guided participants in operating the telescope and understanding solar features.

For many, this was their first direct glimpse at the Sun through a scientific instrument, turning abstract concepts into vivid, observable reality.

<div style="display: flex; flex-wrap: wrap; gap: 15px; margin-top: 10px; justify-content: center;">
  <a href="assests/images/facilities/telescope.jpg" target="_blank">
    <img src="assests/images/facilities/telescope.jpg" alt="Telescope 1" style="width: auto; height: 200px; object-fit: cover; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.08);">
  </a>
  <a href="assests/images/facilities/sun.jpg" target="_blank">
    <img src="assests/images/facilities/sun.jpg" alt="Sun Observation" style="width: auto; height: 200px; object-fit: cover; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.08);">
  </a>
  <a href="assests/images/facilities/telescope_roof.jpg" target="_blank">
    <img src="assests/images/facilities/telescope_roof.jpg" alt="Telescope Setup on Roof" style="width: auto; height: 200px; object-fit: cover; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.08);">
  </a>
</div>

---

<style>
  h1, h2, h3 {
    color: #2a7ae2;
    font-family: 'Segoe UI', 'Arial', sans-serif;
  }
  ul {
    margin-bottom: 0;
  }
  /* make embedded slides and images responsive to avoid horizontal overflow */
  #varunTalkSlideshow, #lectureSeriesSlideshow,
  #varunTalkSlideshow img, #lectureSeriesSlideshow img,
  #lectureSeriesSlide, #varunTalkSlide {
    max-width: 100%;
    width: 100%;
    height: auto;
  }
  /* reduce fixed 480px containers to scale on small screens */
  #varunTalkSlideshow[style], #lectureSeriesSlideshow[style],
  div[style*="width: 480px"] { width: 100% !important; max-width: 480px; }
</style>
