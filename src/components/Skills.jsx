import React from 'react';
import './Skills.css';
import htmlIcon from '../assets/html.png';
import cssIcon from '../assets/css.png';
import jsIcon from '../assets/js.png';
import pythonIcon from '../assets/python.png';
import csharpIcon from '../assets/csharp.png';

const skills = [
  { title: 'Web Geliştirme', description: 'HTML, CSS, JavaScript ve React ile modern ve kullanıcı dostu web siteleri geliştiriyorum. Arayüz tasarımı yaparken sade ama renkli bir stil benimsemeye çalışıyorum.' },
  { title: 'Uygulama Geliştirme', description: 'Python dili ve PyQt5 kütüphanesiyle masaüstü uygulamaları geliştiriyorum. Uygulamalarımı QSS (Qt Style Sheets) ile görsel olarak tasarlayıp kullanıcı dostu arayüzler oluşturuyorum.' },
  { title: 'Müzik', description: 'Müzik hayatımın vazgeçilmez bir parçası. Gençlik korosunda yer alıyor, aynı zamanda solo performanslar sergiliyorum. Katıldığım birkaç yarışmada birincilik elde ettim. Müziğin, beni ben yapan en güçlü yönlerden biri olduğuna inanıyorum.' }
];

const Skills = () => {
  return (
    <section className="skills-section">
      <h2 className="skills-title">Neler Yapabilirim?</h2>
      <div className="skills-container">
        {skills.map((skill, index) => (
          <div className="card" key={index}>
            <div className="card-inner">
              <div className="card-front">
                <h3>{skill.title}</h3>
              </div>
              <div className="card-back">
                <p>{skill.description}</p>
              </div>
            </div>
          </div>
        ))}
      </div>

        <div className="skills-languages">
        <h3>Bildiğim Diller</h3>
        <div className="language-icons">
          <img src={htmlIcon} alt="HTML" />
          <img src={cssIcon} alt="CSS" />
          <img src={jsIcon} alt="JavaScript" />
          <img src={pythonIcon} alt="Python" />
          <img src={csharpIcon} alt="C#" />
        </div>
      </div>
    </section>
  );
};

export default Skills;
