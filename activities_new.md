---
layout: home
title: Activities
---

<style>
/* Cosmic Timeline UI/UX */
.cosmic-hero {
  background: linear-gradient(135deg, #0b1220 0%, #1a1025 50%, #0b1220 100%);
  padding: 80px 20px;
  border-radius: 24px;
  text-align: center;
  position: relative;
  overflow: hidden;
  box-shadow: 0 12px 32px rgba(11, 18, 32, 0.4);
  margin-bottom: 60px;
  color: #fff;
  box-sizing: border-box;
}
.cosmic-hero::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  background: radial-gradient(circle at 50% 50%, rgba(14, 165, 233, 0.15) 0%, transparent 60%);
  pointer-events: none;
}
.cosmic-hero h1 {
  font-family: 'Sora', sans-serif;
  font-size: 3rem;
  margin: 0 0 15px 0;
  background: linear-gradient(90deg, #fff, #0ea5e9);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-shadow: 0 0 40px rgba(14, 165, 233, 0.4);
  line-height: 1.2;
}
.cosmic-hero p {
  font-size: 1.2rem;
  max-width: 600px;
  margin: 0 auto;
  color: #cbd5e1;
  line-height: 1.6;
}

/* Timeline Architecture */
.cosmic-timeline {
  position: relative;
  max-width: 1000px;
  margin: 0 auto;
  padding: 20px 0 60px 0;
  box-sizing: border-box;
}
.cosmic-timeline::before {
  content: '';
  position: absolute;
  top: 0;
  bottom: 0;
  left: 40px;
  width: 4px;
  background: linear-gradient(to bottom, transparent, #0ea5e9 10%, #1ea286 90%, transparent);
  border-radius: 4px;
  box-shadow: 0 0 15px rgba(14, 165, 233, 0.5);
}

.timeline-event {
  position: relative;
  margin-bottom: 60px;
  padding-left: 100px;
  box-sizing: border-box;
}
.timeline-event:last-child {
  margin-bottom: 0;
}

/* Glowing Nodes */
.timeline-node {
  position: absolute;
  left: 31px;
  top: 24px;
  width: 22px;
  height: 22px;
  background: #0ea5e9;
  border-radius: 50%;
  border: 4px solid #fff;
  box-shadow: 0 0 0 4px rgba(14, 165, 233, 0.2), 0 0 15px rgba(14, 165, 233, 0.6);
  z-index: 1;
  transition: all 0.4s ease;
}
.timeline-event:hover .timeline-node {
  background: #1ea286;
  box-shadow: 0 0 0 6px rgba(30, 162, 134, 0.3), 0 0 25px rgba(30, 162, 134, 0.8);
  transform: scale(1.2);
}

/* Glassmorphism Event Cards */
.timeline-content {
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 20px;
  padding: 30px;
  box-shadow: 0 8px 24px rgba(15, 36, 61, 0.06);
  transition: transform 0.4s ease, box-shadow 0.4s ease;
  position: relative;
  overflow: hidden;
  box-sizing: border-box;
  word-wrap: break-word;
  overflow-wrap: break-word;
}
.timeline-content::before {
  content: '';
  position: absolute;
  top: 0; left: 0; width: 6px; height: 100%;
  background: linear-gradient(to bottom, #0ea5e9, #1ea286);
}
.timeline-event:hover .timeline-content {
  transform: translateY(-5px);
  box-shadow: 0 16px 40px rgba(15, 36, 61, 0.12);
}

/* Event Headers */
.event-date {
  display: inline-block;
  font-size: 0.85rem;
  font-weight: 700;
  color: #0ea5e9;
  text-transform: uppercase;
  letter-spacing: 1px;
  margin-bottom: 8px;
  background: rgba(14, 165, 233, 0.1);
  padding: 6px 14px;
  border-radius: 999px;
}
.timeline-content h2 {
  margin: 0 0 15px 0;
  font-size: 1.6rem;
  color: #0f243d;
  font-family: 'Sora', sans-serif;
  line-height: 1.3;
}
.timeline-content p {
  color: #475569;
  font-size: 1rem;
  line-height: 1.7;
  margin-bottom: 20px;
}

/* Fact Tags */
.event-facts {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  margin-bottom: 24px;
}
.fact-tag {
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  padding: 8px 16px;
  border-radius: 12px;
  font-size: 0.9rem;
  color: #334155;
  display: flex;
  flex-direction: column;
  box-sizing: border-box;
  max-width: 100%;
}
.fact-tag strong {
  color: #0f243d;
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 2px;
}

/* Slideshow & Grids */
.media-container {
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 4px 16px rgba(0,0,0,0.1);
  background: #0b1220;
  margin-top: 20px;
  max-width: 100%;
}
.slideshow-btn {
  background: rgba(255, 255, 255, 0.2) !important;
  backdrop-filter: blur(4px);
  border: 1px solid rgba(255,255,255,0.4) !important;
  color: #fff !important;
  width: 44px !important;
  height: 44px !important;
  font-size: 1.2rem !important;
  transition: all 0.3s ease !important;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}
.slideshow-btn:hover {
  background: rgba(255, 255, 255, 0.4) !important;
  transform: translateY(-50%) scale(1.1) !important;
}
.grid-image-link img {
  border-radius: 12px !important;
  transition: transform 0.3s ease, box-shadow 0.3s ease !important;
}
.grid-image-link:hover img {
  transform: scale(1.05) !important;
  box-shadow: 0 12px 24px rgba(15, 36, 61, 0.2) !important;
}

/* Mobile Responsiveness fixes for text overflow */
@media (max-width: 768px) {
  .cosmic-hero { padding: 40px 15px; border-radius: 16px; }
  .cosmic-hero h1 { font-size: 1.8rem; }
  .cosmic-hero p { font-size: 1rem; }
  .cosmic-timeline::before { left: 15px; }
  .timeline-node { left: 6px; width: 18px; height: 18px; }
  .timeline-event { padding-left: 40px; margin-bottom: 40px; }
  .timeline-content { padding: 16px; }
  .timeline-content h2 { font-size: 1.25rem; }
  .timeline-content p { font-size: 0.95rem; line-height: 1.5; }
  .fact-tag { padding: 6px 12px; font-size: 0.85rem; }
  .media-container { height: 280px !important; }
}
</style>


<header class="cosmic-hero">
  <h1>Explore Our Universe</h1>
  <p>Journey through the latest astronomical events, immersive workshops, and observational sessions at UPES.</p>
</header>

<div class="cosmic-timeline">

  <!-- Event 1: NWDSA -->
  <div class="timeline-event">
    <div class="timeline-node"></div>
    <div class="timeline-content">
      <span class="event-date">February 24-26, 2026</span>
      <h2>National Workshop on Data Science in Astronomy</h2>
      <p>Organized at UPES with academic support from IUCAA. The workshop blended keynote lectures, guided hands-on labs, and participant-led project sessions. Participants worked with real astronomical datasets, strengthening practical skills in data handling, visualization, and time-series analysis using Python.</p>
      
      <div class="event-facts">
        <div class="fact-tag"><strong>Venue</strong>UPES, Dehradun</div>
        <div class="fact-tag"><strong>Format</strong>Talks + Hands-on + Poster Sessions</div>
        <div class="fact-tag"><strong>Status</strong>Successfully Completed</div>
      </div>

      <div class="media-container" style="position: relative; width: 100%; height: 400px;">
        <img src="assests/images/cache/NWDSA/DSCF0007.JPG" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: contain; transition: opacity 0.8s ease;" id="nwdsaSlideA">
        <img src="" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: contain; transition: opacity 0.8s ease; opacity: 0;" id="nwdsaSlideB">
        <button onclick="prevNwdsaSlide()" class="slideshow-btn" style="position: absolute; top: 50%; left: 10px; transform: translateY(-50%); border-radius: 50%; cursor: pointer;">&#8592;</button>
        <button onclick="nextNwdsaSlide()" class="slideshow-btn" style="position: absolute; top: 50%; right: 10px; transform: translateY(-50%); border-radius: 50%; cursor: pointer;">&#8594;</button>
      </div>
    </div>
  </div>

  <!-- Event 2: Night Sky Observation -->
  <div class="timeline-event">
    <div class="timeline-node"></div>
    <div class="timeline-content">
      <span class="event-date">December 2, 2025</span>
      <h2>Night Sky Observation (NSO)</h2>
      <p>Offering students and enthusiasts a direct observational astronomy experience under the evening sky. Participants observed key celestial targets through telescope-guided sessions and received live explanations on sky navigation, star identification, and observation practices.</p>
      
      <div class="event-facts">
        <div class="fact-tag"><strong>Format</strong>Guided Night Observation</div>
        <div class="fact-tag"><strong>Focus</strong>Telescope orientation & constellation tracking</div>
      </div>

      <div class="media-container" style="position: relative; width: 100%; height: 420px;">
        <img src="assests/images/cache/NSO/DSCF8471.jpg" loading="lazy" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: contain; transition: opacity 0.8s ease;" id="nsoSlideA">
        <img src="" loading="lazy" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: contain; transition: opacity 0.8s ease; opacity: 0;" id="nsoSlideB">
        <button onclick="prevNsoSlide()" class="slideshow-btn" style="position: absolute; top: 50%; left: 10px; transform: translateY(-50%); border-radius: 50%; cursor: pointer;">&#8592;</button>
        <button onclick="nextNsoSlide()" class="slideshow-btn" style="position: absolute; top: 50%; right: 10px; transform: translateY(-50%); border-radius: 50%; cursor: pointer;">&#8594;</button>
      </div>
    </div>
  </div>

  <!-- Event 3: National Space Day -->
  <div class="timeline-event">
    <div class="timeline-node"></div>
    <div class="timeline-content">
      <span class="event-date">August 22, 2025</span>
      <h2>National Space Day Guest Lecture</h2>
      <p>On the occasion of the 2nd National Space Day, Prof. Varun Sheel (Head, Planetary Science Division, PRL) delivered a special talk, sharing profound insights into planetary science and ongoing research initiatives in India.</p>

      <div class="event-facts">
        <div class="fact-tag"><strong>Speaker</strong>Prof. Varun Sheel (PRL)</div>
        <div class="fact-tag"><strong>Venue</strong>Buzz-II (Room #9104)</div>
      </div>

      <div class="media-container" style="position: relative; width: 100%; height: 400px; max-width: 600px; margin: 20px auto 0;">
        <img src="assests/images/cache/varun_talk/slide1.jpg" loading="lazy" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; transition: opacity 0.6s;" id="varunTalkSlide">
        <button onclick="prevVarunTalkSlide()" class="slideshow-btn" style="position: absolute; top: 50%; left: 10px; transform: translateY(-50%); border-radius: 50%; cursor: pointer;">&#8592;</button>
        <button onclick="nextVarunTalkSlide()" class="slideshow-btn" style="position: absolute; top: 50%; right: 10px; transform: translateY(-50%); border-radius: 50%; cursor: pointer;">&#8594;</button>
      </div>
    </div>
  </div>

  <!-- Event 4: ARIES Trip -->
  <div class="timeline-event">
    <div class="timeline-node"></div>
    <div class="timeline-content">
      <span class="event-date">April 2025</span>
      <h2>Student Expedition to ARIES, Nainital</h2>
      <p>A group of undergraduate students undertook a memorable academic expedition to the Aryabhatta Research Institute of Observational Sciences (ARIES). They interacted with professional astronomers, gained insights into exo-planet detection, and observed operations at India's largest optical telescope (DOT) and the International Liquid Mirror Telescope (ILMT).</p>
      
      <div style="display: flex; flex-wrap: wrap; gap: 15px; margin-top: 24px; justify-content: center;">
        <a href="assests/images/cache/ARIES_TRIP_2025/WhatsApp Image 2025-04-10 at 16.08.42_49bae8cc.jpg" target="_blank" class="grid-image-link">
          <img src="assests/images/cache/ARIES_TRIP_2025/WhatsApp Image 2025-04-10 at 16.08.42_49bae8cc.jpg" loading="lazy" style="width: auto; height: 180px; max-width: 100%; object-fit: cover;">
        </a>
        <a href="assests/images/cache/ARIES_TRIP_2025/IMG-20250413-WA0017.jpg" target="_blank" class="grid-image-link">
          <img src="assests/images/cache/ARIES_TRIP_2025/IMG-20250413-WA0017.jpg" loading="lazy" style="width: auto; height: 180px; max-width: 100%; object-fit: cover;">
        </a>
        <a href="assests/images/cache/ARIES_TRIP_2025/IMG-20250413-WA0051.jpg" target="_blank" class="grid-image-link">
          <img src="assests/images/cache/ARIES_TRIP_2025/IMG-20250413-WA0051.jpg" loading="lazy" style="width: auto; height: 180px; max-width: 100%; object-fit: cover;">
        </a>
        <a href="assests/images/cache/ARIES_TRIP_2025/WhatsApp Image 2025-04-10 at 15.30.12_ad61e5fc.jpg" target="_blank" class="grid-image-link">
          <img src="assests/images/cache/ARIES_TRIP_2025/WhatsApp Image 2025-04-10 at 15.30.12_ad61e5fc.jpg" loading="lazy" style="width: auto; height: 180px; max-width: 100%; object-fit: cover;">
        </a>
      </div>
    </div>
  </div>

  <!-- Event 5: Lecture Series -->
  <div class="timeline-event">
    <div class="timeline-node"></div>
    <div class="timeline-content">
      <span class="event-date">March 2025</span>
      <h2>Weekly Lecture Series on Astrophysics</h2>
      <p>An ongoing initiative introducing students to astronomy and astrophysics. Open to all, the series explores stellar evolution, black holes, and modern observational techniques, sparking curiosity and interdisciplinary engagement.</p>
      
      <div class="event-facts">
        <div class="fact-tag"><strong>Speakers</strong>Dr. Balendra P. Singh, Dr. Nitesh Kumar, Dr. Prince Sharma, Dr. Arka Chatterjee, Dr. Suvankar R. Chowdhury, Dr. Raju RoyChowdhury</div>
      </div>

      <div class="media-container" style="position: relative; width: 100%; height: 500px; max-width: 480px; margin: 20px auto 0; background: #eee;">
        <img src="assests/images/cache/LECTURE_SERIES_2025/nitesh_talk_poster.jpg" loading="lazy" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: contain; transition: opacity 0.6s;" id="lectureSeriesSlide">
        <button onclick="prevLectureSeriesSlide()" class="slideshow-btn" style="position: absolute; top: 50%; left: 10px; transform: translateY(-50%); border-radius: 50%; cursor: pointer;">&#8592;</button>
        <button onclick="nextLectureSeriesSlide()" class="slideshow-btn" style="position: absolute; top: 50%; right: 10px; transform: translateY(-50%); border-radius: 50%; cursor: pointer;">&#8594;</button>
      </div>
      <div id="lectureSeriesCaption" style="text-align: center; font-size: 0.95em; color: #555; margin-top: 12px; font-weight: 500;">
        Lecture 2 by Dr. Nitesh Kumar on "<em>Measuring the Universe: The Cosmic Ladder</em>"
      </div>
    </div>
  </div>

  <!-- Event 6: Sky Gazing -->
  <div class="timeline-event">
    <div class="timeline-node"></div>
    <div class="timeline-content">
      <span class="event-date">February 2025</span>
      <h2>Sky-Gazing with In-House 12-inch Telescope</h2>
      <p>A sky-gazing session giving students a rare opportunity to explore the skies from campus. The event featured a guided solar observation session, where students safely viewed the Sun through a solar filter, observing sunspots and experiencing the dynamic nature of our nearest star.</p>
      
      <div style="display: flex; flex-wrap: wrap; gap: 15px; margin-top: 24px; justify-content: center;">
        <a href="assests/images/cache/facilities/telescope.jpg" target="_blank" class="grid-image-link">
          <img src="assests/images/cache/facilities/telescope.jpg" loading="lazy" style="width: auto; height: 180px; max-width: 100%; object-fit: cover;">
        </a>
        <a href="assests/images/cache/facilities/sun.jpg" target="_blank" class="grid-image-link">
          <img src="assests/images/cache/facilities/sun.jpg" loading="lazy" style="width: auto; height: 180px; max-width: 100%; object-fit: cover;">
        </a>
        <a href="assests/images/cache/facilities/telescope_roof.jpg" target="_blank" class="grid-image-link">
          <img src="assests/images/cache/facilities/telescope_roof.jpg" loading="lazy" style="width: auto; height: 180px; max-width: 100%; object-fit: cover;">
        </a>
      </div>
    </div>
  </div>

</div>


<!-- JS Slideshow Logic (Ported exactly from old version) -->
<script>
  // --- NWDSA Slideshow ---
  const nwdsaImages = [
    "assests/images/cache/NWDSA/DSCF0007.JPG", "assests/images/cache/NWDSA/DSCF0333.JPG",
    "assests/images/cache/NWDSA/DSCF0590.JPG", "assests/images/cache/NWDSA/DSCF0643.JPG",
    "assests/images/cache/NWDSA/DSCF0704.JPG", "assests/images/cache/NWDSA/DSCF0963.JPG",
    "assests/images/cache/NWDSA/DSCF1124.JPG", "assests/images/cache/NWDSA/DSCF1203.JPG",
    "assests/images/cache/NWDSA/DSCF1240.JPG", "assests/images/cache/NWDSA/DSCF1397.JPG",
    "assests/images/cache/NWDSA/DSCF1432.JPG", "assests/images/cache/NWDSA/DSCF1451.JPG",
    "assests/images/cache/NWDSA/DSCF1457.JPG", "assests/images/cache/NWDSA/DSCF9589.JPG",
    "assests/images/cache/NWDSA/DSCF9620.JPG", "assests/images/cache/NWDSA/DSCF9680.JPG",
    "assests/images/cache/NWDSA/DSCF9918.JPG", "assests/images/cache/NWDSA/DSCF9922.JPG",
    "assests/images/cache/NWDSA/DSCF9982.JPG", "assests/images/cache/NWDSA/DSCF9994.JPG",
    "assests/images/cache/NWDSA/UPES-1.JPG", "assests/images/cache/NWDSA/UPES-2.JPG"
  ];
  let nwdsaIndex = 0; let nwdsaActiveLayer = 'A';
  function showNwdsaSlide(idx) {
    const slideA = document.getElementById('nwdsaSlideA');
    const slideB = document.getElementById('nwdsaSlideB');
    if (!slideA || !slideB) return;
    const current = nwdsaActiveLayer === 'A' ? slideA : slideB;
    const next = nwdsaActiveLayer === 'A' ? slideB : slideA;
    next.src = nwdsaImages[idx];
    const preloadImg = new Image(); preloadImg.src = nwdsaImages[(idx + 1) % nwdsaImages.length];
    requestAnimationFrame(() => { next.style.opacity = 1; current.style.opacity = 0; nwdsaActiveLayer = nwdsaActiveLayer === 'A' ? 'B' : 'A'; });
  }
  function prevNwdsaSlide() { nwdsaIndex = (nwdsaIndex - 1 + nwdsaImages.length) % nwdsaImages.length; showNwdsaSlide(nwdsaIndex); }
  function nextNwdsaSlide() { nwdsaIndex = (nwdsaIndex + 1) % nwdsaImages.length; showNwdsaSlide(nwdsaIndex); }
  setInterval(() => { nextNwdsaSlide(); }, 3800);

  // --- NSO Slideshow ---
  const nsoImages = [
    "assests/images/cache/NSO/DSCF8471.jpg", "assests/images/cache/NSO/DSCF8474.jpg",
    "assests/images/cache/NSO/DSCF8484.jpg", "assests/images/cache/NSO/DSCF8512.jpg",
    "assests/images/cache/NSO/DSCF8525.jpg", "assests/images/cache/NSO/DSCF8584.JPG",
    "assests/images/cache/NSO/DSCF8585.JPG", "assests/images/cache/NSO/DSCF8605.JPG",
    "assests/images/cache/NSO/DSCF8615.JPG", "assests/images/cache/NSO/DSCF8625.JPG",
    "assests/images/cache/NSO/DSCF8658.jpg", "assests/images/cache/NSO/DSCF8659.jpg",
    "assests/images/cache/NSO/DSCF8697.jpg", "assests/images/cache/NSO/DSCF8705.jpg",
    "assests/images/cache/NSO/DSCF8723.jpg"
  ];
  let nsoIndex = 0; let nsoActiveLayer = 'A';
  function showNsoSlide(idx) {
    const slideA = document.getElementById('nsoSlideA');
    const slideB = document.getElementById('nsoSlideB');
    if (!slideA || !slideB) return;
    const current = nsoActiveLayer === 'A' ? slideA : slideB;
    const next = nsoActiveLayer === 'A' ? slideB : slideA;
    next.src = nsoImages[idx];
    const preloadImg = new Image(); preloadImg.src = nsoImages[(idx + 1) % nsoImages.length];
    requestAnimationFrame(() => { next.style.opacity = 1; current.style.opacity = 0; nsoActiveLayer = nsoActiveLayer === 'A' ? 'B' : 'A'; });
  }
  function prevNsoSlide() { nsoIndex = (nsoIndex - 1 + nsoImages.length) % nsoImages.length; showNsoSlide(nsoIndex); }
  function nextNsoSlide() { nsoIndex = (nsoIndex + 1) % nsoImages.length; showNsoSlide(nsoIndex); }
  setInterval(() => { nextNsoSlide(); }, 4000);

  // --- Varun Talk Slideshow ---
  const varunTalkImages = [
    "assests/images/cache/varun_talk/slide1.jpg", "assests/images/cache/varun_talk/slide2.jpg",
    "assests/images/cache/varun_talk/slide3.jpg", "assests/images/cache/varun_talk/slide4.jpg"
  ];
  let varunTalkIndex = 0; let varunTalkSlide = null;
  function showVarunTalkSlide(idx) {
    if (!varunTalkSlide) varunTalkSlide = document.getElementById('varunTalkSlide');
    if (varunTalkSlide) {
      varunTalkSlide.style.opacity = 0;
      setTimeout(() => { varunTalkSlide.src = varunTalkImages[idx]; varunTalkSlide.style.opacity = 1; }, 300);
    }
  }
  function prevVarunTalkSlide() { varunTalkIndex = (varunTalkIndex - 1 + varunTalkImages.length) % varunTalkImages.length; showVarunTalkSlide(varunTalkIndex); }
  function nextVarunTalkSlide() { varunTalkIndex = (varunTalkIndex + 1) % varunTalkImages.length; showVarunTalkSlide(varunTalkIndex); }
  setInterval(() => { nextVarunTalkSlide(); }, 4000);

  // --- Lecture Series Slideshow ---
  const lectureSeriesImages = [
    { src: "assests/images/cache/LECTURE_SERIES_2025/nitesh_talk_poster.jpg", caption: 'Lecture 2 by Dr. Nitesh Kumar on "<em>Measuring the Universe: The Cosmic Ladder</em>"' },
    { src: "assests/images/cache/LECTURE_SERIES_2025/prince_talk.jpeg", caption: 'Lecture 3 by Dr. Prince Sharma on "<em>Life Cycle of Stars</em>"' },
    { src: "assests/images/cache/LECTURE_SERIES_2025/suvankar.jpg", caption: 'Lecture 5 by Dr. Suvankar R. Chowdhury on "<em>Inward Bound: From Rutherford to Large Hadron Collider</em>"' },
    { src: "assests/images/cache/LECTURE_SERIES_2025/raju_talk.png", caption: 'Lecture 6 by Dr. Raju Roychowdhury on "<em>The Einstein Window: A Voyage in Spacetime</em>"' }
  ];
  let lectureSeriesIndex = 0; let lectureSeriesSlide = null; let lectureSeriesCaption = null;
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
  function prevLectureSeriesSlide() { lectureSeriesIndex = (lectureSeriesIndex - 1 + lectureSeriesImages.length) % lectureSeriesImages.length; showLectureSeriesSlide(lectureSeriesIndex); }
  function nextLectureSeriesSlide() { lectureSeriesIndex = (lectureSeriesIndex + 1) % lectureSeriesImages.length; showLectureSeriesSlide(lectureSeriesIndex); }
  setInterval(() => { nextLectureSeriesSlide(); }, 4000);
</script>

<!-- Universal Lightbox (Copied exactly from old version) -->
<style>
  #lightbox-modal { display: none; position: fixed; z-index: 999999; left: 0; top: 0; width: 100%; height: 100%; background: rgba(0, 0, 0, 0.9); justify-content: center; align-items: center; animation: modalFadeIn 0.3s ease; }
  .modal-content { position: relative; width: 100%; height: 100%; display: flex; justify-content: center; align-items: center; }
  .modal-img { max-width: 90%; max-height: 90vh; object-fit: contain; border-radius: 8px; box-shadow: 0 4px 24px rgba(0,0,0,0.5); animation: imageZoomIn 0.3s ease; background: transparent; }
  .close { position: absolute; top: 20px; right: 30px; color: #fff; font-size: 40px; font-weight: bold; cursor: pointer; background: transparent; border: none; z-index: 1000000; line-height: 1; transition: transform 0.2s ease, color 0.2s; }
  .close:hover { transform: scale(1.1); color: #ddd; }
  .prev-btn, .next-btn { position: absolute; top: 50%; transform: translateY(-50%); color: #fff; font-size: 30px; cursor: pointer; background: rgba(255, 255, 255, 0.1); border: none; border-radius: 50%; width: 60px; height: 60px; display: flex; align-items: center; justify-content: center; transition: background 0.3s ease, transform 0.2s ease; z-index: 1000000; backdrop-filter: blur(4px); }
  .prev-btn:hover, .next-btn:hover { background: rgba(255, 255, 255, 0.25); transform: translateY(-50%) scale(1.05); }
  .prev-btn { left: 30px; } .next-btn { right: 30px; }
  @keyframes modalFadeIn { from { opacity: 0; } to { opacity: 1; } }
  @keyframes imageZoomIn { from { transform: scale(0.95); opacity: 0; } to { transform: scale(1); opacity: 1; } }
  @media (max-width: 768px) { .prev-btn, .next-btn { display: none; } .close { top: 15px; right: 20px; font-size: 35px; } .modal-img { max-width: 95%; max-height: 95vh; } }
</style>
<script>
  document.addEventListener('DOMContentLoaded', function() {
    const modal = document.createElement('div');
    modal.id = 'lightbox-modal';
    modal.innerHTML = `
      <div class="modal-content">
        <span class="close">&times;</span>
        <img class="modal-img" src="" alt="">
        <button class="prev-btn">&larr;</button>
        <button class="next-btn">&rarr;</button>
      </div>
    `;
    document.body.appendChild(modal);

    const modalImg = modal.querySelector('.modal-img');
    const closeBtn = modal.querySelector('.close');
    const prevBtn = modal.querySelector('.prev-btn');
    const nextBtn = modal.querySelector('.next-btn');
    let currentItems = [];
    let currentIndex = 0;

    function showModal(src) {
      modalImg.src = src;
      modal.style.display = 'flex';
      document.body.style.overflow = 'hidden';
      modal.style.animation = 'modalFadeIn 0.3s ease';
    }

    document.querySelectorAll('a[href$=".jpg"], a[href$=".JPG"], a[href$=".jpeg"], a[href$=".png"]').forEach(a => {
      a.addEventListener('click', function(e) {
        e.preventDefault();
        const container = this.closest('div');
        if (container) { currentItems = Array.from(container.querySelectorAll('a[href$=".jpg"], a[href$=".JPG"], a[href$=".jpeg"], a[href$=".png"]')).map(el => el.href); }
        else { currentItems = [this.href]; }
        currentIndex = currentItems.indexOf(this.href);
        showModal(this.href);
      });
    });

    closeBtn.addEventListener('click', () => { modal.style.display = 'none'; document.body.style.overflow = 'auto'; });
    prevBtn.addEventListener('click', (e) => { e.stopPropagation(); if (currentItems.length > 0) { currentIndex = (currentIndex - 1 + currentItems.length) % currentItems.length; showModal(currentItems[currentIndex]); } });
    nextBtn.addEventListener('click', (e) => { e.stopPropagation(); if (currentItems.length > 0) { currentIndex = (currentIndex + 1) % currentItems.length; showModal(currentItems[currentIndex]); } });
    
    // Attach slideshow click to open modal
    function attachSlideshowClick(id, imagesVar, indexVar, isObjArray) {
      const container = document.getElementById(id);
      if (container) {
        container.style.cursor = 'pointer';
        container.addEventListener('click', () => {
          if (typeof window[imagesVar] !== 'undefined') { currentItems = isObjArray ? window[imagesVar].map(obj => obj.src) : window[imagesVar]; }
          currentIndex = typeof window[indexVar] !== 'undefined' ? window[indexVar] : 0;
          if (currentItems.length > 0) showModal(currentItems[currentIndex]);
        });
      }
    }
    attachSlideshowClick('nwdsaSlideshow', 'nwdsaImages', 'nwdsaIndex', false);
    attachSlideshowClick('nsoSlideshow', 'nsoImages', 'nsoIndex', false);
    attachSlideshowClick('varunTalkSlideshow', 'varunTalkImages', 'varunTalkIndex', false);
    attachSlideshowClick('lectureSeriesSlideshow', 'lectureSeriesImages', 'lectureSeriesIndex', true);

    modal.addEventListener('click', (e) => { if (e.target === modal || e.target.classList.contains('modal-content')) closeBtn.click(); });
  });
</script>
