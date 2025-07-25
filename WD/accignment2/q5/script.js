let availableSeats = 10;

function bookTicket() {
  const tickets = parseInt(document.getElementById("tickets").value);
  if (tickets <= 0) {
    alert("Please enter valid number of tickets.");
    return false;
  }
  if (tickets > availableSeats) {
    alert("Not enough seats available.");
    return false;
  }

  
  availableSeats -= tickets;
  document.getElementById("available").textContent = availableSeats;
  alert("Ticket booked successfully!");
  return false; // Prevent form submission to stay on page
}
