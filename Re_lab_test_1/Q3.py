#!/usr/bin/env python3
"""
create_product_page.py

Writes an index.html file that shows a dynamic product list using a JavaScript array.
Each product displays Name, Price, and an "Add to Cart" button that shows an alert when clicked.
Then opens the generated page in the default browser.
"""

import os
import webbrowser
from pathlib import Path
import textwrap

HTML_CONTENT = textwrap.dedent("""\
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Dynamic Product List</title>
  <style>
    :root{
      --bg:#f6f7fb;
      --card:#ffffff;
      --muted:#6b7280;
      --accent:#2563eb;
      --shadow: 0 6px 18px rgba(16,24,40,0.06);
      --radius:12px;
      font-family: Inter, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
    }
    body{
      margin:0;
      background:var(--bg);
      color:#0f172a;
      padding:32px;
      line-height:1.4;
    }
    .container{
      max-width:960px;
      margin:0 auto;
    }
    header{
      display:flex;
      align-items:center;
      justify-content:space-between;
      gap:16px;
      margin-bottom:22px;
    }
    h1{
      margin:0;
      font-size:1.4rem;
      letter-spacing:0.2px;
    }
    .cart-info{
      background:var(--card);
      padding:10px 14px;
      border-radius:10px;
      box-shadow:var(--shadow);
      font-size:0.95rem;
    }
    /* product grid */
    .grid{
      display:grid;
      grid-template-columns:repeat(auto-fill,minmax(220px,1fr));
      gap:18px;
    }
    .card{
      background:var(--card);
      border-radius:var(--radius);
      padding:14px;
      box-shadow:var(--shadow);
      display:flex;
      flex-direction:column;
      gap:10px;
    }
    .thumbnail{
      height:120px;
      background:linear-gradient(135deg,#eef2ff,#fef3c7);
      border-radius:10px;
      display:flex;
      align-items:center;
      justify-content:center;
      font-weight:600;
      color:var(--muted);
      font-size:0.95rem;
    }
    .meta{
      display:flex;
      justify-content:space-between;
      align-items:center;
      gap:10px;
      font-size:0.98rem;
    }
    .name{
      font-weight:600;
    }
    .price{
      color:var(--accent);
      font-weight:700;
    }
    .actions{
      margin-top:auto;
      display:flex;
      gap:8px;
    }
    button{
      cursor:pointer;
      border:0;
      padding:8px 10px;
      border-radius:8px;
      font-weight:600;
    }
    .btn-add{
      background:var(--accent);
      color:white;
      flex:1;
      box-shadow:0 6px 12px rgba(37,99,235,0.14);
    }
    .btn-view{
      background:transparent;
      border:1px solid #e6edf8;
      color:var(--muted);
      min-width:70px;
    }
    footer{
      margin-top:20px;
      font-size:0.9rem;
      color:var(--muted);
    }
    @media (max-width:520px){
      body{padding:18px;}
      .thumbnail{height:100px;font-size:0.85rem;}
    }
  </style>
</head>
<body>
  <div class="container">
    <header>
      <h1>Product Catalog</h1>
      <div class="cart-info" id="cartInfo">Cart: <span id="cartCount">0</span> items</div>
    </header>

    <main>
      <div class="grid" id="productGrid">
        <!-- Products will be injected here by JavaScript -->
      </div>
    </main>

    <footer>
      Simple dynamic product list — each product shows Name, Price, and an "Add to Cart" button.
    </footer>
  </div>

  <script>
    // JavaScript array of products (edit/add as needed)
    const products = [
      { id: 1, name: "Wireless Headphones", price: 129.99 },
      { id: 2, name: "Smart Watch", price: 199.50 },
      { id: 3, name: "Portable Speaker", price: 79.00 },
      { id: 4, name: "USB-C Charger", price: 24.99 },
      { id: 5, name: "Laptop Sleeve", price: 34.75 },
      { id: 6, name: "Mechanical Keyboard", price: 109.00 }
    ];

    // Simple cart state (count only for this example)
    const cart = {
      items: [],
      add(product){
        this.items.push(product);
        updateCartUI();
        alert("Added to cart");
      }
    };

    // DOM references
    const grid = document.getElementById("productGrid");
    const cartCount = document.getElementById("cartCount");

    function formatPrice(p){
      // Format price in a simple way (USD). You can change locale/currency as needed.
      return p.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 });
    }

    function createProductCard(product){
      const card = document.createElement("div");
      card.className = "card";

      const thumb = document.createElement("div");
      thumb.className = "thumbnail";
      // Simple placeholder: initials
      const initials = product.name.split(" ").map(w => w[0]).slice(0,2).join("");
      thumb.textContent = initials;

      const meta = document.createElement("div");
      meta.className = "meta";

      const name = document.createElement("div");
      name.className = "name";
      name.textContent = product.name;

      const price = document.createElement("div");
      price.className = "price";
      price.textContent = "₹ " + formatPrice(product.price); // uses INR symbol — change if needed

      meta.appendChild(name);
      meta.appendChild(price);

      const actions = document.createElement("div");
      actions.className = "actions";

      const addBtn = document.createElement("button");
      addBtn.className = "btn-add";
      addBtn.textContent = "Add to Cart";
      addBtn.addEventListener("click", () => cart.add(product));

      const viewBtn = document.createElement("button");
      viewBtn.className = "btn-view";
      viewBtn.textContent = "View";
      viewBtn.addEventListener("click", () => {
        // Simple view action - can be enhanced
        alert(product.name + "\\nPrice: ₹ " + formatPrice(product.price));
      });

      actions.appendChild(addBtn);
      actions.appendChild(viewBtn);

      card.appendChild(thumb);
      card.appendChild(meta);
      card.appendChild(actions);

      return card;
    }

    function renderProducts(){
      grid.innerHTML = "";
      products.forEach(p => {
        grid.appendChild(createProductCard(p));
      });
    }

    function updateCartUI(){
      cartCount.textContent = cart.items.length;
    }

    // initial render
    renderProducts();
  </script>
</body>
</html>
""")

def main():
    out_path = Path.cwd() / "index.html"
    out_path.write_text(HTML_CONTENT, encoding="utf-8")
    abs_path = out_path.resolve().as_uri()
    print(f"Generated {out_path}")
    print("Opening in default browser...")
    webbrowser.open(abs_path)

if __name__ == "__main__":
    main()
