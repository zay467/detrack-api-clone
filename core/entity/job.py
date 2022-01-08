from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
import uuid
from .job_item import JobItem

from sqlalchemy.orm import relationship

class Job(BaseModel):
    detrack_type :str
    primary_job_status:str
    open_to_marketplace:str
    marketplace_offer:str
    do_number:str
    date:datetime
    start_date:datetime
    status:str
    job_release_time:datetime
    job_time:str
    time_window:str
    job_received_date:datetime
    tracking_number:str
    order_number:str
    job_type:str
    job_sequence:str
    job_fee:str
    address_lat:str
    address_lng:str
    address:str
    company_name:str
    address_1:str
    address_2:str
    address_3:str
    postal_code:str
    city:str
    state:str
    country:str
    billing_address:str
    deliver_to_collect_from:str
    last_name:str
    phone_number:str
    sender_phone_number:str
    fax_number:str
    instructions:str
    assign_to:str
    notify_email:str
    webhook_url:str
    zone:str
    customer:str
    account_number:str
    job_owner:str
    invoice_number:str
    payment_mode:str
    payment_amount:str
    group_id:str
    group_name:str
    vendor_name:str
    source:str
    weight:int
    parcel_width:int
    parcel_length:int
    parcel_height:int
    cubic_meter:float
    boxes:int
    cartons:int
    pieces:int
    envelopes:int
    pallets:int
    bins:int
    trays:int
    bundles:int
    rolls:int
    number_of_shipping_labels:int
    attachment_url:str
    carrier:str
    auto_reschedule:str
    eta_time:datetime
    depot:str
    depot_contact:str
    department:str
    sales_person:str
    identification_number:str
    bank_prefix:str
    run_number:str
    pick_up_from:str
    pick_up_time:str
    pick_up_lat:str
    pick_up_lng:str
    pick_up_address:str
    pick_up_address_1:str
    pick_up_address_2:str
    pick_up_address_3:str
    pick_up_city:str
    pick_up_state:str
    pick_up_country:str
    pick_up_postal_code:str
    pick_up_zone:str
    job_price:float
    insurance_price:float
    insurance_coverage:str
    total_price:float
    payer_type:str
    remarks:str
    service_type:str
    warehouse_address:str
    destination_time_window:str
    door:str
    time_zone:str
    vehicle_type:str
    items:list[JobItem]
    
    pod_time:datetime
    class Config():
        orm_mode = True