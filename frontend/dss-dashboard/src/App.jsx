import { useEffect, useState }  from "react";

function App(){
  const [items,setItems] = useState([]);
  const [error, setError] = useState(null);
  
  useEffect (()=>{
    fetch("http://127.0.0.1:8000/api/items/")
    .then((res)=>{
      if(!res.ok){
        throw new Error("gagal mengambil data DSS");
      }
      return res.json();
    })
    .then((data) => setItems(data))
    .catch((err) => setError(err.message));
  },[]);

  if (error){
    return <p style={{ color:"red"}}>{error}</p>
  }

  return (
    <div style={{ padding: "20px" }}>
      <h1>DSS Purchase Order</h1>

      <table border="1" cellPadding="8">
        <thead>
          <tr>
            <th>Item Code</th>
            <th>Item Name</th>
            <th>Stock</th>
            <th>Avg Monthly Sales</th>
            <th>DOI</th>
            <th>Recommendation</th>
          </tr>
        </thead>
        <tbody>
          {items.map((item) => (
            <tr key={item.item_code}>
              <td>{item.item_code}</td>
              <td>{item.item_name}</td>
              <td>{item.current_stock}</td>
              <td>{item.avg_monthly_sales}</td>
              <td>{item.doi}</td>
              <td>{item.recomendation}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;