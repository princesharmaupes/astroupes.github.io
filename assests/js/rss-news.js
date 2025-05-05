const feeds = {
    "NASA Breaking News": "https://www.nasa.gov/rss/dyn/breaking_news.rss",
    "James Webb": "https://webbtelescope.org/news/rss",
    "NuSTAR": "https://www.nasa.gov/rss/dyn/mission_pages/nustar.rss",
    "Swift": "https://www.nasa.gov/rss/dyn/mission_pages/swift.rss",
    "Fermi": "https://fermi.gsfc.nasa.gov/rss/news.xml"
  };
  
  const container = document.getElementById("floating-news");
  const feedSelector = document.createElement("select");
  
  for (let name in feeds) {
    const option = document.createElement("option");
    option.value = feeds[name];
    option.textContent = name;
    feedSelector.appendChild(option);
  }
  
  feedSelector.onchange = () => loadFeed(feedSelector.value);
  container.appendChild(feedSelector);
  
  const listContainer = document.createElement("div");
  container.appendChild(listContainer);
  
  function loadFeed(rssUrl) {
    const proxy = "https://api.rss2json.com/v1/api.json?rss_url=";
    fetch(proxy + encodeURIComponent(rssUrl))
      .then(res => res.json())
      .then(data => {
        let html = "<ul>";
        data.items.slice(0, 5).forEach(item => {
          html += `<li><a href="${item.link}" target="_blank">${item.title}</a></li>`;
        });
        html += "</ul>";
        listContainer.innerHTML = html;
      })
      .catch(() => {
        listContainer.innerHTML = "<p>Failed to load news. Try again later.</p>";
      });
  }
  
  // Load default feed
  loadFeed(feedSelector.value);
  