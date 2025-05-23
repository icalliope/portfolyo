import React from 'react';
import './About.css';
import Lottie from 'lottie-react';
import leftAnim from '../assets/code.json';
import rightAnim from '../assets/Animation - singer.json';
import slideAnim from '../assets/squirrel.json';

const About = () => {
  return (
    <section className="about-section">
      <div className="about-container">

        <div className="about-animation left">
          <Lottie animationData={leftAnim} loop={true} />
        </div>


        <div className="about-card">
          <h2>Ben Kimim?</h2>
          <p>
            Ben İrem İclal Karapınar, 4 Ağustos 2004 tarihinde Konya'da doğdum.
            İlkokul, ortaokul ve liseyi Konya'da okuduktan sonra Ekim 2023'te Balıkesir Üniversitesi'nde
            Bilgisayar Mühendisliği okumaya başladım. Web geliştirme, oyun geliştirme ve uygulama geliştirme
            gibi alanlara ilgi duyuyorum. Ayrıca Gençlik Korosundayım ve müzikle ilgilenmeyi çok seviyorum.
          </p>
        </div>

        <div className="about-animation right">
          <Lottie animationData={rightAnim} loop={true} />
        </div>
      </div>

        <div className="slide-animation">
  <Lottie animationData={slideAnim} loop={true} />
</div>

    </section>

  );
};

export default About;
