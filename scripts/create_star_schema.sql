CREATE TABLE dim_customer AS
SELECT DISTINCT 
    "Customer Id" AS customer_id,
    "Customer Country" AS customer_country,
    "Customer Segment" AS customer_segment,
    "Customer City" AS customer_city,
    "Customer State" AS customer_state,
    "Customer Street" AS customer_street
FROM stg_logistics;

ALTER TABLE dim_customer ADD PRIMARY KEY (customer_id);



CREATE TABLE dim_product AS
SELECT DISTINCT 
    "Product Card Id" AS product_card_id,
    "Product Name" AS product_name,
    "Product Price" AS product_price,
    "Category Id" AS category_id,
    "Category Name" AS category_name,
    "Department Id" AS department_id,
    "Department Name" AS department_name,
    "Product Image" AS product_image,
    "Product Category Id" AS product_category_id
FROM stg_logistics;

ALTER TABLE dim_product ADD PRIMARY KEY (product_card_id);



CREATE TABLE dim_order_details AS
SELECT DISTINCT 
    "Order Id" AS order_id,
    "Order Country" AS order_country,
    "Order City" AS order_city,
    "Order Region" AS order_region,
    "Order State" AS order_state,
    "Order Status" AS order_status,
    "Shipping Mode" AS shipping_mode,
    "Delivery Status" AS delivery_status,
    "Late_delivery_risk" AS late_delivery_risk,
    "Type" AS order_type,
    "Order Date" AS order_date,
    "Ship Date" AS ship_date,
    "Market" AS market
FROM stg_logistics;

ALTER TABLE dim_order_details ADD PRIMARY KEY (order_id);



CREATE TABLE fact_order AS
SELECT 
    "Order Id" AS order_id,
    "Order Item Id" AS order_item_id,
    "Customer Id" AS customer_id,
    "Product Card Id" AS product_card_id,
    "Order Item Product Price" AS order_item_product_price,
    "Order Item Profit Ratio" AS order_item_profit_ratio,
    "Order Item Quantity" AS order_item_quantity,
    "Order Item Cardprod Id" AS order_item_cardprod_id,
    "Profit Per Order" AS profit_per_order,
    "Order Item Discount" AS order_item_discount,
    "Order Item Discount Rate" AS order_item_discount_rate,
    "Days for shipping (real)" AS days_for_shipping_real,
    "Days for shipment (scheduled)" AS days_for_shipment_scheduled,
    "Sales per customer" AS sales_per_customer,
    "Gross Sales" AS gross_sales,
    "Net Sales" AS net_sales
FROM stg_logistics;


ALTER TABLE fact_order ADD PRIMARY KEY (order_item_id);
ALTER TABLE fact_order ADD CONSTRAINT fk_customer FOREIGN KEY (customer_id) REFERENCES dim_customer(customer_id);
ALTER TABLE fact_order ADD CONSTRAINT fk_product FOREIGN KEY (product_card_id) REFERENCES dim_product(product_card_id);
ALTER TABLE fact_order ADD CONSTRAINT fk_order_details FOREIGN KEY (order_id) REFERENCES dim_order_details(order_id);