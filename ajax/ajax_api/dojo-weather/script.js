var coordinates = {
    "Burbank": [34.180840, -118.308968],
    "Dallas": [32.7767, -96.7970],
    "Chicago": [41.8781, -87.6298],
    "San Jose": [37.3387, -121.8853]
};

var cities = ["Burbank", "Chicago", "Dallas", "San Jose"];

var tempUnit = document.querySelector("#temp-units").value.toString()[1];


//Date Formatting from MDN Web Docs by Mozilla [https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getDay]
//Make sure the dates are set correctly on the window
var date = new Date(); //gets current date-time
date.setDate(date.getDate() + 2); //increment date by 1
document.querySelector("#day3-header").innerText = (new Intl.DateTimeFormat("en-US", { weekday: "long" }).format(date));
date.setDate(date.getDate() + 1);
document.querySelector("#day4-header").innerText = (new Intl.DateTimeFormat("en-US", { weekday: "long" }).format(date));


async function getWeather(element) {
    let lat = coordinates[element.innerText][0];
    let lon = coordinates[element.innerText][1];
    let units = (tempUnit == 'C') ? "metric" : "imperial";
    let apiURL = `https://api.openweathermap.org/data/2.5/forecast?lat=${lat}&lon=${lon}&units=${units}&appid={apiKey}`;
    let response = await fetch(apiURL);
    let weatherData = await response.json();
    
    console.log(weatherData);

    updateWindow(weatherData, element);
}


function updateWindow(data, element) {
    date = new Date();
    //Update the city selectors
    document.querySelector(".cities").innerHTML = "";
    document.querySelector("#current-city").innerText = element.innerText;
    for(var i = 0; i < cities.length; i++){
        if(element.innerText == cities[i]){
            continue;
        } else {
            document.querySelector(".cities").innerHTML += "<h3 onclick=\"getWeather(this)\">" + cities[i] + "</h3>";
        }
    }

    //Update the weather icons with the api data
    var weatherTabs = document.querySelectorAll(".weather-tab");
    var index = 0;
    for(var i = 0; index < weatherTabs.length && i < 40; i++){
        if(i == 0){
            weatherTabs[index].querySelector("img").src = getImgSrcByWeather(data.list[0].weather[0].main);
            weatherTabs[index].querySelector("p").innerText = getDescOfWeather(data.list[0].weather[0].main);
            weatherTabs[index].querySelector(".high").innerText = Math.round(data.list[0].main.temp_max).toString() + "\u00b0";
            weatherTabs[index].querySelector(".low").innerText = Math.round(data.list[0].main.temp_min).toString() + "\u00b0";
            index++;
        } else {
            date.setTime(data.list[i].dt * 1000);
            if(date.getUTCHours() == 0){
                weatherTabs[index].querySelector("img").src = getImgSrcByWeather(data.list[i].weather[0].main);
                weatherTabs[index].querySelector("p").innerText = getDescOfWeather(data.list[i].weather[0].main);
                weatherTabs[index].querySelector(".high").innerText = Math.round(data.list[i].main.temp_max).toString() + "\u00b0";
                weatherTabs[index].querySelector(".low").innerText = Math.round(data.list[i].main.temp_min).toString() + "\u00b0";

                index++;
            } else {
                continue;
            }
        }
    }
}

function getImgSrcByWeather(weatherText){
    switch(weatherText) {
        case "Rain":
            return "assets/some_rain.png";
        case "Clouds":
            return "assets/some_clouds.png";
        case "Clear":
            return "assets/some_sun.png";
        default:
            return "assets/some_sun.png";
    }
}

function getDescOfWeather(weatherText){
    switch(weatherText) {
        case "Rain":
            return "Some Rain";
        case "Clouds":
            return "Some Clouds";
        case "Clear":
            return "Some Sun";
        default:
            return "Some Sun";
    }
}

function hideCookieWindow() {
    document.querySelector(".cookie-popup").style.display = "none";
}

function changeUnits(unit) {
    //Get all elements with the high-and-low class
    var temps = document.querySelectorAll(".high-and-low");

    for(var i = 0; i < temps.length; i++){
        //Get the integer value from the temperature
        var high = parseInt(temps[i].children[0].innerText);
        var low = parseInt(temps[i].children[1].innerText);

        //Find if it's going to C or F
        if(unit.value == "\u00B0C"){
            //Convert to celsius
            high = Math.round((high - 32) * 0.5556);
            low = Math.round((low - 32) * 0.5556);

            //Store new data
            temps[i].children[0].innerText = high + "\u00B0";
            temps[i].children[1].innerText = low + "\u00B0";
            tempUnit = 'C';
        } else if (unit.value == "\u00B0F") {
            //Convert to fahrenheit
            high = Math.round((high * 1.8) + 32);
            low = Math.round((low * 1.8) + 32);

            //store new data
            temps[i].children[0].innerText = high + "\u00B0";
            temps[i].children[1].innerText = low + "\u00B0";

            tempUnit = 'F';
        }
    }
}
