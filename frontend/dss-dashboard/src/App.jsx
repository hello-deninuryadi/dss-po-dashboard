import { useEffect, useState }  from "react";

function App(){
  const [items,setItems] = useState([]);
  const [error, setError] = useState(null);
  const [showRecomendation,setShowRecomendation] = useState(true)
  const [overrideHistory, setOverrideHistory] = useState([])
  const [showHistoryFor, setShowHistoryFor] = useState(null)


  // Override Manual 
  const [overrides, setOverrides] = useState({})

  // Amnbil rekomendasi yang di tampilkan (System / override)
  const getDisplayedRecomendation = (item) => {
    return overrides[item.item_code]?.value || item.recomendation;
  }

const fetchOverrideHistory = (item_code) =>{
  fetch(`http://127.0.0.1:8000/api/override/history/${item_code}/`)
  .then((res) => res.json())
  .then((data) => {
    setOverrideHistory(data);
    setShowHistoryFor(item_code);
  });
};


  //Fetch Data
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

  const getRecomendationStyle = (rec) =>{
    if (rec === "LAYAK PO") return { color : "green", fontWeight : "bold"};
    if (rec === "MONITOR") return {color : "orange", fontWeight : "bold"};
    if (rec === "TUNDA PO") return {color : "red", fontWeight : "bold"};
  }
  
  
  return (
    <div style={{ padding: "20px" }}>
      <h1>DSS Rekomendasi Purchase Order</h1>
      <p>Berbasis Days of Inventory on Hand (DOI)</p>

      <button onClick={()=> setShowRecomendation(!showRecomendation)}
      style={{marginBottom: "10px"}} >
        {showRecomendation ? "Sembunyikan Rekomendasi" : "Tampilkan Rekomendasi"}
      </button>

      <table border="1" cellPadding="8">
        <thead>
          <tr>
            <th>Item Code</th>
            <th>Item Name</th>
            <th>Stock</th>
            <th>Avg Monthly Sales</th>
            <th>DOI</th>
            {
              showRecomendation && (
                <th>Recomendation</th>
              )
            }
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

              {
                showRecomendation && (
                  <td style={getRecomendationStyle(
                    getDisplayedRecomendation(item))}
                  >
                    {getDisplayedRecomendation(item)}
                  <br/>

                  <button 
                  onClick={() => {
                    const value = prompt("Override Rekomendasi DSS\n\nMasukan Pilihan\nLAYAK PO / MONITOR / TUNDA PO");
                    const reason = prompt("Alasaan Override\n\nJelaskan alasan bisnis melakukan Override :");
                    if (value && reason){
                      fetch("http://127.0.0.1:8000/api/override/",{
                        method : "POST",
                        headers : {
                          "Content-Type" : "application/json",
                        },
                        body:   JSON.stringify({
                          item: item.id,
                          override_value : value,
                          reason: reason,
                        }),
                      });
                      setOverrides({
                        ...overrides,
                        [item.item_code] : {value, reason},
                      });
                    }
                  }}
                  style={{marginTop : "6px"}}
                  >
                    Override
                  </button>
                  <button
                    onClick={() => fetchOverrideHistory(item.item_code)}
                    style={{padding: "10px", marginLeft : "6px", marginTop: "6px" , fontSize : "16px"}}
                  >
                    Lihat Riwayat
                  </button>
                  {overrides[item.item_code] && (
                      <div style={{
                        fontSize : "12px",
                        fontStyle : "italic"
                      }}>
                        overriden
                      </div>
                  )}

                  {overrides[item.item_code]?.reason && (
                    <div style={{
                      fontSize : "12px",
                      color : "#555",
                      marginTop : "2px"
                    }}>
                      alasan : {overrides[item.item_code].reason}
                    </div>
                  )}
                  </td>
                )
              }

            </tr>
          ))}
        </tbody>
      </table>
          {showHistoryFor && (
            <div style = {{ marginTop : "20px" }}>
              <h3>Riwayat Override - {showHistoryFor}</h3>
            
            {overrideHistory.length === 0 ? (
              <p>Tidak ada riwayat Override.</p>
            ) : (
              <ul>
                {overrideHistory.map((h) =>(
                  <li key={h.id}>
                    <strong>{h.override_value}</strong> - {h.reason}
                    <span style={{ fontSize : "12px", color : "#555"}}>
                      {" "}
                      ({new Date(h.created_at).toLocaleString()})
                    </span>
                  </li>
                ))}
              </ul>
            )}
            </div>
          )}

    </div>
  );
}

export default App;