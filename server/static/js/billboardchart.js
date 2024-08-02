const dateinput = document.getElementById('date-calendar-input')
dateinput.addEventListener("change", (e) => {
    const selectedDate = e.target.value;
    location.href = `/billboardchart/${selectedDate}`;
});