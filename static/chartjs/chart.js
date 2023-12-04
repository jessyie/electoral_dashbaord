// Function to fetch and update chart data
function updateCharts(selectedYear, region) {

  fetch(`/update_charts?year=${selectedYear}&region=${''}`)
  .then(response => response.json())
  .then(data => {
    
    // Update chart configuration and data based on the fetched data

    document.querySelector('#parliamentTotal').innerHTML = data.tSum + " : VALID VOTES";
    document.querySelector('#presidentialTotal').innerHTML = data.tSum2 + " : VALID VOTES"; 
    
    // Get the select element
    var selectElement = document.getElementById("regionSelection");

    // Store the currently selected region
    var selectedRegion = selectElement.value;

    // Get the "Region" option element
    // var regionOption = document.getElementById("regionOption");

    // Clear existing options except the "Region" option
    while (selectElement.options.length > 1) {
        selectElement.remove(1);
    }

    //Iterate over the fetched data and create new options
    for (var i = 0; i < data.graph1BX.length; i++) {
        var option = document.createElement("option");
        option.textContent = data.graph1BX[i];
        selectElement.appendChild(option);
    }

    // Set the value of the select element to the stored selected region
    // selectElement.value = selectedRegion;

    // // Ensure the "Region" option is always the first option
    // selectElement.insertBefore(regionOption, selectElement.options[0]);


    chart1.update({
      chart: {
        type: 'bar'
      },
      title: {
        text: 'Total Valid Votes Per Region (Parliament)',
        align: 'left'
      },

      xAxis: {
        categories: data.graph1AX,
        title: {
          text: 'Regions'
        },
        gridLineWidth: 1,
        lineWidth: 0
      },
      yAxis: {
        min: 0,
        title: {
          text: 'Total Valid Votes',
          align: 'high'
        },
        labels: {
          overflow: 'justify'
        },
        gridLineWidth: 0
      },
      tooltip: {
        valueSuffix: '' 
      },
      plotOptions: {
        bar: {
          borderRadius: '50%',
          dataLabels: {
            enabled: true
          },
          groupPadding: 0.1
        }
      },
      legend: {
        layout: 'vertical',
        align: 'right',
        verticalAlign: 'top',
        x: -40,
        y: 30,
        floating: true,
        borderWidth: 1,
        backgroundColor:
        Highcharts.defaultOptions.legend.backgroundColor || '#FFFFFF',
        shadow: true
      },
      credits: {
        enabled: false
      },
      series: [{
        name: 'Valid Votes',
        data: data.graph1AY
      }]
    });

    chart1b.update({
      chart: {
        type: 'bar'
      },
      title: {
        text: 'Total Valid Votes Per Region (Presidential)',
        align: 'left'
      },

      xAxis: {
        categories: data.graph1BX,
        title: {
          text: 'Regions'
        },
        gridLineWidth: 1,
        lineWidth: 0
      },
      yAxis: {
        min: 0,
        title: {
          text: 'Total Valid Votes',
          align: 'high'
        },
        labels: {
          overflow: 'justify'
        },
        gridLineWidth: 0
      },
      tooltip: {
        valueSuffix: '' 
      },
      plotOptions: {
        bar: {
          borderRadius: '50%',
          dataLabels: {
            enabled: true
          },
          groupPadding: 0.1
        }
      },
      legend: {
        layout: 'vertical',
        align: 'right',
        verticalAlign: 'top',
        x: -40,
        y: 30,
        floating: true,
        borderWidth: 1,
        backgroundColor:
        Highcharts.defaultOptions.legend.backgroundColor || '#FFFFFF',
        shadow: true
      },
      credits: {
        enabled: false
      },
      series: [{
        name: 'Valid Votes',
        data: data.graph1BY
      }]
    });

    chart2.update({
      chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false
      },
      title: {
        text: 'Total Valid Votes Per Political Party (Parliament)'
      },
      
      plotOptions: {
        pie: {
          allowPointSelect: true,
          cursor: 'pointer',
          dataLabels: {                  
            enabled: true,
            color: '#000000',
            connectorColor: '#000000',
          }
        }
      },
      series: [{
        type: 'pie',
        showInLegend: true,
        name: 'Valid Votes',
        data: data.tSumCA
      }]

    });

    chart2b.update({
      chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false
      },
      title: {
        text: 'Total Valid Votes Per Political Party (Presidential)'
      },
      
      plotOptions: {
        pie: {
          allowPointSelect: true,
          cursor: 'pointer',
          dataLabels: {
            enabled: true,
            color: '#000000',
            connectorColor: '#000000',
          }
        }
      },
      series: [{
        type: 'pie',
        showInLegend: true,
        name: 'Valid Votes',
        data: data.tSumDA
      }]
    });

    const datum =  data.df_grouped3z;

    // Extract categories (first column) and column names (header row)
    const categories = datum.map(item => item[0]);
    const columnNames = data.graph2AX;

    // Extract series data (exclude the first row which contains column names)
    const seriesData = datum.slice(0).map(item => item.slice(1));

    chart3.update({
      chart: {
        type: 'column'
      },
      title: {
        text: 'Total Valid Votes for Each Political Party Per Region(Parliament)',
        style: {
          fontSize: '17px',
          fontWeight: 'bold'
        }
      },
      xAxis: {
        categories: categories,
        min: 0,
        max: 10,
        scrollbar: {
          enabled: true
        },
      },
      yAxis: {
        title: {
          text: 'Valid Votes'
        }
      },
      credits: {
        enabled: false
      },
      tooltip: {
        headerFormat: '<b>{point.x}</b><br/>',
        pointFormat: '{series.name}: {point.y}<br/>Total: {point.stackTotal}'
      },
      plotOptions: {
        column: {
          stacking: 'normal',
        }
      },
      series: columnNames.map((columnName, index) => ({
        name: columnName,
        data: seriesData.map(dataSeries => dataSeries[index]),
        showInLegend: false,
      }))

    });


    const datum2 =  data.df_grouped4z;


    // Extract categories (first column) and column names (header row)
    const categories2 = datum2.map(item => item[0]);
    const columnNames2 = data.graph2BX;

    // Extract series data (exclude the first row which contains column names)
    const seriesData2 = datum2.slice(0).map(item => item.slice(1));

    chart3b.update({
      chart: {
        type: 'column'
      },
      title: {
        text: 'Total Valid Votes for Each Political Party Per Region(Presidential)',
        style: {
          fontSize: '17px',
          fontWeight: 'bold'
        }
      },
      xAxis: {
        categories: categories2,
        min: 0,
        max: 10,
        scrollbar: {
          enabled: true
        },
      },
      yAxis: {
        title: {
          text: 'Valid Votes'
        }
      },
      credits: {
        enabled: false
      },
      tooltip: {
        headerFormat: '<b>{point.x}</b><br/>',
        pointFormat: '{series.name}: {point.y}<br/>Total: {point.stackTotal}'
      },
      plotOptions: {
        column: {
          stacking: 'normal',
        }
      },
      series: columnNames2.map((columnName, index) => ({
        name: columnName,
        data: seriesData2.map(dataSeries => dataSeries[index]),
        showInLegend: false,
      }))
    });

    chart4.update({
      chart: {
        type: 'bar'
      },
      title: {
        text: 'Population Demographics',
        align: 'left'
      },
      subtitle: {
        text: '',
        align: 'left'
    },
      xAxis: {
        categories: data.graph1AX2P,
        title: {
          text: 'Regions'
        },
        gridLineWidth: 1,
        lineWidth: 0
      },
      yAxis: {
        min: 0,
        title: {
          text: 'NOTE: Only 2020 Population Demographics Data is available',
          align: 'high'
        },
        labels: {
          overflow: 'justify'
        },
        gridLineWidth: 0
      },
      tooltip: {
        valueSuffix: '' 
      },
      plotOptions: {
        bar: {
          borderRadius: '50%',
          dataLabels: {
            enabled: true
          },
          groupPadding: 0.1
        }
      },
      legend: {
        layout: 'vertical',
        align: 'right',
        verticalAlign: 'top',
        x: -40,
        y: 30,
        floating: true,
        borderWidth: 1,
        backgroundColor:
        Highcharts.defaultOptions.legend.backgroundColor || '#FFFFFF',
        shadow: true
      },
      credits: {
        enabled: false
      },
      series: [{
        name: 'Population Demographics',
        data: data.graph1AY2P
      }]
    });

  })
  
  updateMap(region, selectedYear)
};


// Helper function to get the CSRF token from cookies
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

function changeChartYear() {
  const yearSelector = document.querySelector("#yearSelection")
  const regionSelector = document.querySelector("#regionSelection")
  
  activeYear = yearSelector.value || '2020'
  activeRegion = regionSelector.value 
  
  updateCharts(activeYear, activeRegion);
  
}



  // Function to fetch and update chart data
function updateCharts2(year, selectedRegion) {

  fetch(`/update_charts?year=${year}&region=${selectedRegion}`)
  .then(response => response.json())
  .then(data => {
    
    // Update chart configuration and data based on the fetched data

    document.querySelector('#parliamentTotal').innerHTML = data.tSumR + " : VALID VOTES";
    document.querySelector('#presidentialTotal').innerHTML = data.tSum2R + " : VALID VOTES";
    

    var selectElement = document.getElementById("regionSelection");
    var selectCensus = document.getElementById("censusSelection");

    // Store the currently selected region
    var selectedRegion = selectElement.value;

    // Get the "Region" option element
    // var regionOption = document.getElementById("regionOption");

    // Clear existing options except the "Region" option
    while (selectElement.options.length > 1) {
        selectElement.remove(1); 

      }

    //Iterate over the fetched data and create new options
    for (var i = 0; i < data.graph1BX.length; i++) {
        var option = document.createElement("option");
        option.textContent = data.graph1BX[i];
        selectElement.appendChild(option);
    }

    // Set the value of the select element to the stored selected region
    selectElement.value = selectedRegion;
    


    chart1.update({
      chart: {
        type: 'bar'
      },
      title: {
        text: 'Total Valid Votes Per Constituency (Parliament)',
        align: 'left'
      },

      xAxis: {
        categories: data.graphSub1AX,
        min: 0,
        max: 5,
        scrollbar: {
          enabled: true
        },
        title: {
          text: 'Constituencies'
        },
        gridLineWidth: 1,
        lineWidth: 0
      },
      yAxis: {
        min: 0,
        title: {
          text: 'Total Valid Votes',
          align: 'high'
        },
        labels: {
          overflow: 'justify'
        },
        gridLineWidth: 0
      },
      tooltip: {
        valueSuffix: '' 
      },
      plotOptions: {
        bar: {
          borderRadius: '50%',
          dataLabels: {
            enabled: true
          },
          groupPadding: 0.1
        }
      },
      legend: {
        layout: 'vertical',
        align: 'right',
        verticalAlign: 'top',
        x: -40,
        y: 30,
        floating: true,
        borderWidth: 1,
        backgroundColor:
        Highcharts.defaultOptions.legend.backgroundColor || '#FFFFFF',
        shadow: true
      },
      credits: {
        enabled: false
      },
      series: [{
        name: 'Valid Votes',
        data: data.graphSub1AY
      }]
    });

    chart1b.update({
      chart: {
        type: 'bar'
      },
      title: {
        text: 'Total Valid Votes Per Constituency (Presidential)',
        align: 'left'
      },

      xAxis: {
        categories: data.graphSub1BX,
        min: 0,
        max: 5,
        scrollbar: {
          enabled: true
        },
        title: {
          text: 'Constituencies'
        },
        gridLineWidth: 1,
        lineWidth: 0
      },
      yAxis: {
        min: 0,
        title: {
          text: 'Total Valid Votes',
          align: 'high'
        },
        labels: {
          overflow: 'justify'
        },
        gridLineWidth: 0
      },
      tooltip: {
        valueSuffix: '' 
      },
      plotOptions: {
        bar: {
          borderRadius: '50%',
          dataLabels: {
            enabled: true
          },
          groupPadding: 0.1
        }
      },
      legend: {
        layout: 'vertical',
        align: 'right',
        verticalAlign: 'top',
        x: -40,
        y: 30,
        floating: true,
        borderWidth: 1,
        backgroundColor:
        Highcharts.defaultOptions.legend.backgroundColor || '#FFFFFF',
        shadow: true
      },
      credits: {
        enabled: false
      },
      series: [{
        name: 'Valid Votes',
        data: data.graphSub1BY
      }]
    });

    chart2.update({
      chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false
      },
      title: {
        text: 'Total Valid Votes Per Political Party Constituency(Parliament)',
        style: {
          fontSize: '17px',
          fontWeight: 'bold'
        }
      },
      
      plotOptions: {
        pie: {
          allowPointSelect: true,
          cursor: 'pointer',
          dataLabels: {                  
            enabled: true,
            color: '#000000',
            connectorColor: '#000000',
          }
        }
      },
      series: [{
        type: 'pie',
        showInLegend: true,
        name: 'Valid Votes',
        data: data.tSumCAP
      }]

    });

    chart2b.update({
      chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false
      },
      title: {
        text: 'Total Valid Votes Per Political Party Constituency(Presidential)',
        style: {
          fontSize: '17px',
          fontWeight: 'bold'
        }
      },
      
      plotOptions: {
        pie: {
          allowPointSelect: true,
          cursor: 'pointer',
          dataLabels: {
            enabled: true,
            color: '#000000',
            connectorColor: '#000000',
          }
        }
      },
      series: [{
        type: 'pie',
        showInLegend: true,
        name: 'Valid Votes',
        data: data.tSumDAP
      }]
    });

    const datum3 =  data.df_grouped3zP;

    // Extract categories (first column) and column names (header row)
    const categories3 = datum3.map(item => item[0]);
    const columnNames3 = data.graph2AXP;

    // Extract series data (exclude the first row which contains column names)
    const seriesData3 = datum3.slice(0).map(item => item.slice(1));

    chart3.update({
      chart: {
        type: 'column'
      },
      title: {
        text: 'Total Valid Votes for Each Political Party Per Constituency(Parliament)',
        style: {
          fontSize: '17px',
          fontWeight: 'bold'
        }
      },
      xAxis: {
        categories: categories3,
        min: 0,
        max: 5,
        scrollbar: {
          enabled: true
        },
      },
      yAxis: {
        title: {
          text: 'Valid Votes'
        }
      },
      credits: {
        enabled: false
      },
      tooltip: {
        headerFormat: '<b>{point.x}</b><br/>',
        pointFormat: '{series.name}: {point.y}<br/>Total: {point.stackTotal}'
      },
      plotOptions: {
        column: {
          stacking: 'normal',
        }
      },
      series: columnNames3.map((columnName, index) => ({
        name: columnName,
        data: seriesData3.map(dataSeries => dataSeries[index]),
        showInLegend: false,
      }))

    });


    const datum4 =  data.df_grouped3zP2;


    // Extract categories (first column) and column names (header row)
    const categories4 = datum4.map(item => item[0]);
    const columnNames4 = data.graph2BXP;

    // Extract series data (exclude the first row which contains column names)
    const seriesData4 = datum4.slice(0).map(item => item.slice(1));

    chart3b.update({
      chart: {
        type: 'column'
      },
      title: {
        text: 'Total Valid Votes for Each Political Party Per Constituency(Presidential)',
        style: {
          fontSize: '17px',
          fontWeight: 'bold'
        }
      },
      xAxis: {
        categories: categories4,
        min: 0,
        max: 5,
        scrollbar: {
          enabled: true
        },
      },
      yAxis: {
        title: {
          text: 'Valid Votes'
        }
      },
      credits: {
        enabled: false
      },
      tooltip: {
        headerFormat: '<b>{point.x}</b><br/>',
        pointFormat: '{series.name}: {point.y}<br/>Total: {point.stackTotal}'
      },
      plotOptions: {
        column: {
          stacking: 'normal',
        }
      },
      series: columnNames4.map((columnName, index) => ({
        name: columnName,
        data: seriesData4.map(dataSeries => dataSeries[index]),
        showInLegend: false,
      }))
    });

    chart4.update({
      chart: {
        type: 'bar'
      },
      title: {
        text: 'Population Demographics',
        align: 'left'
      },
      subtitle: {
        text: '',
        align: 'left'
    },
      xAxis: {
        categories: data.graph1BX2P,
        min: 0,
        max: 5,
        scrollbar: {
          enabled: true
        },
        title: {
          text: 'Constituencies'
        },
        gridLineWidth: 1,
        lineWidth: 0
      },
      yAxis: {
        min: 0,
        title: {
          text: 'NOTE: Only 2020 Population Demographics Data is available',
          align: 'high'
        },
        labels: {
          overflow: 'justify'
        },
        gridLineWidth: 0
      },
      tooltip: {
        valueSuffix: '' 
      },
      plotOptions: {
        bar: {
          borderRadius: '50%',
          dataLabels: {
            enabled: true
          },
          groupPadding: 0.1
        }
      },
      legend: {
        layout: 'vertical',
        align: 'right',
        verticalAlign: 'top',
        x: -40,
        y: 30,
        floating: true,
        borderWidth: 1,
        backgroundColor:
        Highcharts.defaultOptions.legend.backgroundColor || '#FFFFFF',
        shadow: true
      },
      credits: {
        enabled: false
      },
      series: [{
        name: 'Population Demographics',
        data: data.graph1BY2P
      }]
    });
    
  })


  updateMap(selectedRegion, year)
};


// Helper function to get the CSRF token from cookies
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

function changeChartRegion() {
  const yearSelector = document.querySelector("#yearSelection")
  const regionSelector = document.querySelector("#regionSelection")
 
  activeRegion = regionSelector.value || 'Ashanti'
  activeYear = yearSelector.value ||'2020'
  
  updateCharts2(activeYear, activeRegion); 

}


  // Function to fetch and update chart data
function updateCharts3(censusSelected, year, region) {

  fetch(`/selectCensus?census=${censusSelected}&year=${year}&region=${region}`)
  .then(response => response.json())
  .then(data => {

    var selectCensus = document.getElementById("censusSelection");
    var subtitleText = selectCensus.value !== 'Total Pop' ? selectCensus.value + ' %' : '';


     chart4.update({
      chart: {
        type: 'bar'
      },
      title: {
        text: 'Population Demographics',
        align: 'left'
      },
      subtitle: {
        text: subtitleText,
        align: 'left'
    },
      xAxis: {
        categories: data.graph1AX2P,
        min: 0,
        max: 5,
        scrollbar: {
          enabled: true
        },
        title: {
          text: 'Constituencies'
        },
        gridLineWidth: 1,
        lineWidth: 0
      },
      yAxis: {
        min: 0,
        title: {
          text: 'NOTE: Only 2020 Population Demographics Data is available',
          align: 'high'
        },
        labels: {
          overflow: 'justify'
        },
        gridLineWidth: 0
      },
      tooltip: {
        valueSuffix: selectCensus.value !== 'Total Pop' ? '%' : '' 
      },
      plotOptions: {
        bar: {
          borderRadius: '50%',
          dataLabels: {
            enabled: true
          },
          groupPadding: 0.1
        }
      },
      legend: {
        layout: 'vertical',
        align: 'right',
        verticalAlign: 'top',
        x: -40,
        y: 30,
        floating: true,
        borderWidth: 1,
        backgroundColor:
        Highcharts.defaultOptions.legend.backgroundColor || '#FFFFFF',
        shadow: true
      },
      credits: {
        enabled: false
      },
      series: [{
        name: 'Population Demographics',
        data: data.graph1AY2P
      }]
    });

  })
}
      
// Helper function to get the CSRF token from cookies
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

  // Function to fetch and update chart data
function updateCharts4(censusSelected, year, region) {

  fetch(`/selectCensus?census=${censusSelected}&year=${year}&region=${region}`)
  .then(response => response.json())
  .then(data => {

    var selectCensus = document.getElementById("censusSelection");
    var subtitleText = selectCensus.value !== 'Total Pop' ? selectCensus.value + ' %' : '';

     chart4.update({
      chart: {
        type: 'bar'
      },
      title: {
        text: 'Population Demographics',
        align: 'left'
      },
      subtitle: {
        text: subtitleText,
        align: 'left'
    },
      xAxis: {
        categories: data.graph1BX2P,
        min: 0,
        max: 5,
        scrollbar: {
          enabled: true
        },
        title: {
          text: 'Constituencies'
        },
        gridLineWidth: 1,
        lineWidth: 0
      },
      yAxis: {
        min: 0,
        title: {
          text: 'NOTE: Only 2020 Population Demographics Data is available',
          align: 'high'
        },
        labels: {
          overflow: 'justify'
        },
        gridLineWidth: 0
      },
      tooltip: {
        valueSuffix: selectCensus.value !== 'Total Pop' ? '%' : '' 
      },
      plotOptions: {
        bar: {
          borderRadius: '50%',
          dataLabels: {
            enabled: true
          },
          groupPadding: 0.1
        }
      },
      legend: {
        layout: 'vertical',
        align: 'right',
        verticalAlign: 'top',
        x: -40,
        y: 30,
        floating: true,
        borderWidth: 1,
        backgroundColor:
        Highcharts.defaultOptions.legend.backgroundColor || '#FFFFFF',
        shadow: true
      },
      credits: {
        enabled: false
      },
      series: [{
        name: 'Population Demographics',
        data: data.graph1BY2P
      }]
    });

  })
}
      
// Helper function to get the CSRF token from cookies
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

function changeChart_RegionalCensus() {
  const censusSelector = document.querySelector("#censusSelection2")
  const yearSelector = document.querySelector("#yearSelection")
  const regionSelector = document.querySelector("#regionSelection")
  activeCensus = censusSelector.value || 'Total Pop'
  activeRegion = regionSelector.value || 'Ashanti'
  activeYear = yearSelector.value ||'2020'

  if (!activeRegion) {
    updateCharts3(activeCensus, activeYear);
  }else {
    updateCharts3(activeCensus, activeYear, activeRegion);
  }
  

}

function changeChart_DistrictCensus() {
  const censusSelector = document.querySelector("#censusSelection")
  const yearSelector = document.querySelector("#yearSelection")
  const regionSelector = document.querySelector("#regionSelection")
  activeCensus = censusSelector.value || 'Total Pop'
  activeRegion = regionSelector.value || 'Ashanti'
  activeYear = yearSelector.value ||'2020'
  
  updateCharts4(activeCensus, activeYear, activeRegion);

}

