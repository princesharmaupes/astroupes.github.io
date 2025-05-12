---
layout: default
title: Home
---
# ✨ Astronomy & Astrophysics  
### A Sub-Division of the Department of Physics under the Cluster of Applied Science, School of Advanced Engineering  

Explore the universe with us — from the smallest particles to the largest galaxies, we bridge the gap between curiosity and discovery.

<em>Stars have always called to the curious. We, at UPES, turn that call into a career.</em> 

Our B.Sc. in Astronomy and Astrophysics takes you from the fundamentals of physics to the frontiers of space science.  
Explore the mysteries of the universe through data, decode cosmic phenomena, and contribute to real astronomical research — all as part of a dynamic and forward-looking academic environment.

---

## 🌟 What We Offer

- 🎓 **Undergraduate & Postgraduate Programs**  
  Explore the field of Astronomy and Astrophysics through specialized degree tracks with hands-on training in data analysis, simulation, and observational techniques.

- 🚀 **Research Opportunities**  
  Work on real-world projects alongside faculty and researchers, with collaborations across premier institutions like ARIES, IUCAA, and PRL.

- 🌌 **Sky-Gazing & Workshops**  
  Experience the mysteries beyond Earth firsthand through regular public outreach events, night-sky observations, and hands-on sessions with department telescopes.

- 🧑‍🏫 **Academic Excellence**  
Learn from leading researchers and visiting scientists engaged in cutting-edge work on cosmology, high-energy astrophysics, X-ray accretion in compact objects, AI-based stellar cluster analysis and theoretical black hole physics.


---
<!-- Faculty Section -->
<section id="faculty-section" style="padding: 60px 20px; background: #f5f5f5;">
  <h2 style="text-align:center; font-size: 2em;">Faculty</h2>
  <div id="faculty-carousel" style="overflow: hidden; width: 100%; position: relative;">
    <div id="faculty-cards" style="display: flex; transition: transform 0.5s ease-in-out; width: max-content;">
      <div style="background: #e9edf4; border-radius: 15px; width: 300px; padding: 20px; text-align: center; box-shadow: 0 4px 10px rgba(0,0,0,0.1); margin-right: 20px;">
        <img src="assests/images/rawat.png" alt="Dr. Prashant S. Rawat" style="width: 100%; border-radius: 10px;">
        <h3>Dr. Prashant S. Rawat</h3>
        <p><strong>Sr. Associate Professor, School of Applied Science</strong></p>
        <p style="font-size: 0.9em;">Dr. Rawat earned his doctoral degree from the esteemed Physical Research Laboratory (PRL), Ahmedabad....</p>
        <a href="faculty.html#PSRAWAT" class="read-more-button" style="color:rgb(0, 0, 0); text-decoration: none; font-weight: bold;">Read more →</a>
      </div>
      <div style="background: #e9edf4; border-radius: 15px; width: 300px; padding: 20px; text-align: center; box-shadow: 0 4px 10px rgba(0,0,0,0.1); margin-right: 20px;">
        <img src="assests/images/balendra.jpeg" alt="Dr. Balendra P. Singh" style="width: 100%; border-radius: 10px;">
        <h3>Dr. Balendra P. Singh</h3>
        <p><strong>Assistant Professor, School of Applied Science</strong></p>
        <p style="font-size: 0.9em;">Balendra P. Singh specializes in Astrophysics and Astronomy and received his PhD from the Center for Theoretical Physics...</p>
        <a href="faculty.html#BALENDRA" class="read-more-button" style="color:rgb(0, 0, 0); text-decoration: none; font-weight: bold;">Read more →</a>
      </div>
      <div style="background: #e9edf4; border-radius: 15px; width: 300px; padding: 20px; text-align: center; box-shadow: 0 4px 10px rgba(0,0,0,0.1); margin-right: 20px;">
        <img src="assests/images/nitesh.jpeg" alt="Dr. Nitesh Kumar" style="width: 100%; border-radius: 10px;">
        <h3>Dr. Nitesh Kumar</h3>
        <p><strong>Assistant Professor, School of Applied Science</strong></p>
        <p style="font-size: 0.9em;">Dr. Nitesh has done his Ph. D. in Automated Stellar Evolution study from the University of Delhi....</p>
        <a href="faculty.html#NITESH" class="read-more-button" style="color:rgb(0, 0, 0); text-decoration: none; font-weight: bold;">Read more →</a>
      </div>
      <div style="background: #e9edf4; border-radius: 15px; width: 300px; padding: 20px; text-align: center; box-shadow: 0 4px 10px rgba(0,0,0,0.1); margin-right: 20px;">
        <img src="assests/images/prince.png" alt="Dr. Prince Sharma" style="width: 100%; border-radius: 10px;">
        <h3>Dr. Prince Sharma</h3>
        <p><strong>Assistant Professor, School of Applied Science</strong></p>
        <p style="font-size: 0.9em;">Dr. Sharma is an alumunus of Kirorimal College and obtained his Doctorate from University of Delhi....</p>
        <a href="faculty.html#PRINCE" class="read-more-button" style="color:rgb(0, 0, 0); text-decoration: none; font-weight: bold;">Read more →</a>
      </div>
      <div style="background: #e9edf4; border-radius: 15px; width: 300px; padding: 20px; text-align: center; box-shadow: 0 4px 10px rgba(0,0,0,0.1); margin-right: 20px;">
        <img src="assests/images/arka.jpeg" alt="Dr. Arka Chatterjee" style="width: 100%; border-radius: 10px;">
        <h3>Dr. Arka Chatterjee</h3>
        <p><strong>Assistant Professor, School of Applied Science</strong></p>
        <p style="font-size: 0.9em;">Dr. Arka Chatterjee is an Astrophysicist with a PhD in Theoretical Physics from the University of Calcutta....</p>
        <a href="faculty.html#ARKA" class="read-more-button" style="color:rgb(0, 0, 0); text-decoration: none; font-weight: bold;">Read more →</a>
      </div>
    </div>
    <button id="prev-btn" style="position: absolute; top: 50%; left: 10px; transform: translateY(-50%); background: #333; color: #fff; border: none; padding: 10px; cursor: pointer; border-radius: 50%;">&#8249;</button>
    <button id="next-btn" style="position: absolute; top: 50%; right: 10px; transform: translateY(-50%); background: #333; color: #fff; border: none; padding: 10px; cursor: pointer; border-radius: 50%;">&#8250;</button>
  </div>
</section>

<script>
  const facultyCards = document.getElementById('faculty-cards');
  const prevBtn = document.getElementById('prev-btn');
  const nextBtn = document.getElementById('next-btn');

  function getCardScrollWidth() {
    const firstCard = facultyCards.querySelector('.faculty-card');
    if (!firstCard) return 300;
    const style = window.getComputedStyle(firstCard);
    return firstCard.offsetWidth + parseInt(style.marginRight || 0);
  }

  prevBtn.addEventListener('click', () => {
    const scrollAmount = getCardScrollWidth();
    facultyCards.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
  });

  nextBtn.addEventListener('click', () => {
    const scrollAmount = getCardScrollWidth();
    facultyCards.scrollBy({ left: scrollAmount, behavior: 'smooth' });
  });
</script>



---



## 🗞 Recent Highlights

- ✅ *April 2025:* Student visit to ARIES, Nainital.  
<!-- - ✅ *February 2025:* B.Sc. students observed variable stars with new 12-inch telescope   -->
<!-- - ✅ *January 2025:* Faculty paper on stellar classification accepted in MNRAS   -->

➡️ See more in [Recent Activities](activities.md)

---

## 🌟 Join Us

Applications are open for the **B.Sc. (Hons.) Physics** and **M.Sc. Physics** programs.  
Build your career in **Astronomy** and **Astrophysics**.

🔗 [Learn about our academic programs](programs.md)

---

> _"Somewhere, something incredible is waiting to be known."_  
> — Carl Sagan