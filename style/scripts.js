window.parent.document.getElementById('button-17').addEventListener('click', showPopup);
window.parent.document.getElementById('button-17').addEventListener('click', changeText);
window.parent.document.getElementById('popup').addEventListener('click', hidePopup);

function showPopup() {
    window.parent.document.getElementById('popup').style.display = 'block';
    window.parent.document.getElementById('button-17').style.display = 'none';
};
function hidePopup() {
    window.parent.document.getElementById('popup').style.display = 'none';
    window.parent.document.getElementById('button-17').style.display = 'block';
};
var texts = [
       "The Great Barrier Reef, off the coast of Australia, is the world's largest coral reef ecosystem.",
    "The Amazon Rainforest produces 20% of the world's oxygen.",
    "The concept of sustainability dates back to the 18th century when German forester Hans Carl von Carlowitz introduced the term 'Nachhaltigkeit' (sustainability).",
    "Earth's atmosphere is composed of approximately 78% nitrogen, 21% oxygen, and trace amounts of other gases.",
    "The oldest tree in the world is believed to be a Bristlecone Pine in California's White Mountains, estimated to be over 5,000 years old.",
    "The ozone layer, found in the Earth's stratosphere, protects life on Earth by absorbing harmful ultraviolet radiation from the sun.",
    "The Industrial Revolution in the 18th and 19th centuries marked a significant increase in pollution and environmental degradation.",
    "Plastic pollution is a pressing environmental issue, with over 8 million tons of plastic waste entering the oceans every year.",
    "Deforestation contributes to habitat loss, biodiversity loss, and climate change.",
    "The Dust Bowl of the 1930s in the United States was caused by severe drought and unsustainable farming practices.",
    "Antarctica is the coldest, driest, and windiest continent on Earth.",
   " Renewable energy sources such as solar, wind, and hydroelectric power offer sustainable alternatives to fossil fuels.",
    "The Kyoto Protocol, adopted in 1997, aimed to reduce greenhouse gas emissions to combat climate change.",
    "The Aral Sea in Central Asia has drastically shrunk due to excessive water diversion for irrigation.",
    "Overfishing and illegal fishing practices threaten marine biodiversity and fish populations.",
    "Rachel Carson's book 'Silent Spring', published in 1962, sparked the modern environmental movement and led to the ban of the pesticide DDT.",
    "The Chernobyl nuclear disaster in 1986 led to widespread environmental contamination and long-term health effects.",
   " The Paris Agreement, adopted in 2015, aims to limit global warming to well below 2 degrees Celsius above pre-industrial levels."
    "The Pacific Garbage Patch is a vast area of marine debris concentrated by ocean currents.",
   " The Dust Bowl migration in the United States resulted in mass displacement and migration of farmers during the 1930s.",
    "The Clean Air Act of 1970 in the United States aimed to regulate air pollution and improve air quality.",
    "The Exxon Valdez oil spill in 1989 off the coast of Alaska caused extensive damage to marine ecosystems.",
        "The first Earth Day was celebrated on April 22, 1970, marking the beginning of the modern environmental movement.",
    "The ozone layer protects life on Earth by absorbing harmful ultraviolet radiation from the sun.",
    "The Clean Air Act of 1970 led to significant reductions in air pollution and improved air quality in the United States.",
    "Plastic pollution poses a grave threat to marine life, with over 8 million tons of plastic waste entering the oceans annually.",
    "Deforestation contributes to habitat loss, biodiversity decline, and climate change.",
    "Renewable energy sources such as solar and wind power offer sustainable alternatives to fossil fuels.",
    "The Paris Agreement, adopted in 2015, aims to limit global warming to well below 2 degrees Celsius above pre-industrial levels.",
    "Ocean acidification, caused by increased carbon dioxide absorption, threatens marine ecosystems and coral reefs.",
    "The Kyoto Protocol established emissions trading mechanisms to reduce greenhouse gas emissions.",
    "The United Nations Convention on Biological Diversity (CBD) aims to conserve biodiversity and ensure its sustainable use.",
    "Soil erosion, exacerbated by deforestation and unsustainable land use, leads to loss of soil fertility and degradation.",
    "The Dust Bowl migration reshaped demographics and cultural landscapes in the United States.",
    "The Montreal Protocol is regarded as one of the most successful environmental agreements, leading to the phase-out of ozone-depleting substances.",
    "Urbanization and industrialization have led to habitat loss and fragmentation, threatening biodiversity.",
    "The Intergovernmental Panel on Climate Change (IPCC) assesses scientific literature on climate change and its impacts.",
    "Sustainable agriculture practices such as agroforestry and organic farming promote soil health and biodiversity.",
    "Earth Day, first celebrated in 1970, raises awareness about environmental issues and promotes sustainability.",
    "The International Union for Conservation of Nature (IUCN) maintains the Red List of Threatened Species to assess the conservation status of species.",
    "The Dust Bowl migration contributed to demographic shifts and cultural changes in the United States.",
    "The Clean Air Act Amendments of 1990 strengthened air quality standards and regulatory measures in the United States.",
    "The Montreal Protocol successfully phased out the production and use of ozone-depleting substances, leading to the recovery of the ozone layer.",
    "Soil conservation practices such as terracing and cover cropping help prevent soil erosion and improve soil health.",
    "The Clean Water Act established water quality standards and pollution control measures in the United States.",
    "The Dust Bowl prompted federal intervention through programs like the Civilian Conservation Corps (CCC) and the Soil Conservation Service (SCS).",
    "The Rio Earth Summit resulted in agreements on biodiversity, climate change, and sustainable development.".
    ];

function changeText() {
    var randomIndex = Math.floor(Math.random() * texts.length);
    var newText = texts[randomIndex];

    window.parent.document.getElementById('popupText').innerHTML = newText;
};

if (!window.parent.document.querySelector('[class^=icon2]')) {
    var newDiv = document.createElement('span');
            
    newDiv.className  = 'icon2';

    var button = window.parent.document.querySelector('div[id^=tabs-bui][id$=-tabpanel-4] > div > div > div > div > div > div > div> div > div > div > button[kind = "secondary"] > div');

    button.appendChild(newDiv);
};

if (!window.parent.document.querySelector('[class^=icon3]')) {
    var newDiv2 = document.createElement('span');
            
    newDiv2.className  = 'icon3';

    var button2 = window.parent.document.querySelector('div[id^=tabs-bui][id$=-tabpanel-2] > div > div > div > div > div > div > div> div > div > div > button[kind = "secondary"] > div');

    button2.appendChild(newDiv2);
};
                        
function checkScreenWidth() {
  var screenWidth = window.innerWidth || window.parent.document.documentElement.clientWidth || window.parent.document.body.clientWidth;

  if (screenWidth <= 600) {
            window.parent.document.getElementById('project-copyright').style.display = 'none';
            Array.from(window.parent.document.querySelectorAll('button[data-baseweb="tab"] > div > p')).forEach(button => button.style.fontSize = '10px');
  } else {
            window.parent.document.getElementById('project-copyright').style.display = 'block';
  }
}

window.onload = checkScreenWidth;
window.onresize = checkScreenWidth;
