import { useEffect, useState } from "react";

export default function Test() {
  const [message, setMessage] = useState<string>("");
  const [listings, setListings] = useState<RoleListing[]>([]);

  const fetchData = async () => {
    try {
      const response = await fetch("api/hi");
      const data = await response.json();
      console.log(data);
      setMessage(data.message);

      // Process the data or update state with the fetched data
    } catch (error) {
      console.error("Error calling /api/hi:", error);
    }
  };

  const fetchListings = async () => {
    try {
      const response = await fetch("api/listings");
      const { data: listings }: { data: RoleListing[] } = await response.json();
      setListings(listings);
    } catch (error) {
      console.error("Error calling /api/listings:", error);
    }
  };

  useEffect(() => {
    fetchData();
    fetchListings();
  }, []);

  return (
    <div>
      <h1>Test</h1>
      <p>{message}</p>

      <h1>Role listings</h1>
      {listings.map((listing) => (
        <div key={listing.id}>
          <h2>Name {listing.name}</h2>
          <p>Description: {listing.description}</p>
          <p>Start time: {listing.start_time}</p>
          <p>End time: {listing.end_time}</p>
        </div>
      ))}
    </div>
  );
}
