let currentIndex = 0;
const articles = document.querySelectorAll('article');

function showArticle(index) {
  articles.forEach((article, i) => {
    if (i === index) {
      article.dataset.active = 'active';
    } else {
      article.dataset.active = 'inactive';
    }
  });
}

function movepageleft() {
  if (currentIndex > 0) {
    currentIndex--;
  } else {
    currentIndex = articles.length - 1;
  }
  showArticle(currentIndex);
}

function movepageright() {
  if (currentIndex < articles.length - 1) {
    currentIndex++;
  } else {
    currentIndex = 0;
  }
  showArticle(currentIndex);
}

// Initialize by showing the first article
showArticle(currentIndex);



//changer border color

const borderColors = ['#5B9279', '#8AA39B', '#BFDBF7', '#DEFFFC','#ACBFA4','#759AAB', '#1B98E0','#47E5BC', '#3423A6', '#F2F3AE'];

window.onload = () => {
  let style = getComputedStyle(document.body)
  style.getPropertyValue('--dark-color') 
  document.documentElement.style.setProperty('--border-color', borderColors[Math.floor(Math.random()*borderColors.length)]);
}

