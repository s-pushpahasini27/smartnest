# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

# 45 Properties with description, neighborhood, trends
properties = [
    # MUMBAI (3)
    {'id': 1, 'title': 'Bandra Sea View 3BHK', 'location': 'Mumbai, Maharashtra', 'price': 28000000, 'bedrooms': 3, 'bathrooms': 2, 'area': 1450, 'image': 'https://assets.architecturaldigest.in/photos/60083f49d0435267a8df9192/16:9/w_2560,c_limit/mumbai-apartment-pka-interior-design-feature-02-866x487-1366x768.jpg', 'description': 'Stunning sea-facing apartment with open balcony, modular kitchen, and 24/7 security.', 'neighborhood': 'Trendy Bandra West – cafes, gyms, Carter Road promenade, top schools.', 'trends': 'High demand, 10–12% annual appreciation.'},
    {'id': 2, 'title': 'Worli Penthouse', 'location': 'Mumbai, Maharashtra', 'price': 48000000, 'bedrooms': 4, 'bathrooms': 4, 'area': 2800, 'image': 'https://www.killadesign.com/wp-content/uploads/2021/01/Worli-KD-Terrace-03.jpg', 'description': 'Ultra-luxury duplex with private terrace, infinity pool, and concierge service.', 'neighborhood': 'Elite Worli Sea Face – near Atria Mall, 5-star hotels, business hubs.', 'trends': 'Premium segment, 15% YoY growth.'},
    {'id': 3, 'title': 'Andheri Studio', 'location': 'Mumbai, Maharashtra', 'price': 11500000, 'bedrooms': 1, 'bathrooms': 1, 'area': 620, 'image': 'https://jannathomes.com/uploads/gallery/2022/11/23/img_x_500637de498253e58-64087024.jpg', 'description': 'Compact, modern studio ideal for young professionals. Fully furnished.', 'neighborhood': 'Andheri East – near metro, IT parks, malls, airports.', 'trends': 'Affordable, 8% annual rise.'},

    # PUNE (3)
    {'id': 4, 'title': 'Koregaon Park Villa', 'location': 'Pune, Maharashtra', 'price': 19500000, 'bedrooms': 4, 'bathrooms': 3, 'area': 2400, 'image': 'https://img.squareyards.com/secondaryPortal/IN_638786026740313955-2603250417541754.jpeg', 'description': 'Spacious independent villa with lawn, parking, and high-end finishes.', 'neighborhood': 'Posh Koregaon Park – Osho, German Bakery, fine dining, expat community.', 'trends': 'Stable, 9% appreciation.'},
    {'id': 5, 'title': 'Hinjewadi IT Flat', 'location': 'Pune, Maharashtra', 'price': 8500000, 'bedrooms': 2, 'bathrooms': 2, 'area': 1100, 'image': 'https://im.proptiger.com/1/502724/6/eon-homes-images-for-elevation-of-kasturi-housing-eon-homes-11353967.jpeg', 'description': 'Modern 2BHK in gated society with gym, pool, and shuttle to IT parks.', 'neighborhood': 'Hinjewadi Phase 1 – Infosys, TCS, Wipro, food courts.', 'trends': 'IT-driven demand, 7–10% growth.'},
    {'id': 6, 'title': 'Viman Nagar 3BHK', 'location': 'Pune, Maharashtra', 'price': 13500000, 'bedrooms': 3, 'bathrooms': 2, 'area': 1350, 'image': 'https://rohanbuilders.com/wp-content/uploads/2023/02/Rohan-mithila-gallery7.jpg', 'description': 'Well-ventilated corner flat with balcony and covered parking.', 'neighborhood': 'Viman Nagar – Phoenix Mall, airport, international schools.', 'trends': 'Family-friendly, 8% rise.'},

    # NAGPUR (3)
    {'id': 7, 'title': 'Civil Lines Bungalow', 'location': 'Nagpur, Maharashtra', 'price': 16500000, 'bedrooms': 4, 'bathrooms': 3, 'area': 2100, 'image': 'https://4.imimg.com/data4/OG/CO/ANDROID-34999906/product-500x500.jpeg', 'description': 'Grand bungalow with garden and vintage charm.', 'neighborhood': 'Civil Lines – elite area, hospitals, parks.', 'trends': 'Heritage value, 6–8% growth.'},
    {'id': 8, 'title': 'Ramdaspeth Apartment', 'location': 'Nagpur, Maharashtra', 'price': 9800000, 'bedrooms': 3, 'bathrooms': 2, 'area': 1250, 'image': 'https://img.staticmb.com/mbimages/project/Photo_h310_w462/Project-Photo-3-Jagannath-Pride-Thane-5096707_600_800_310_462.jpg', 'description': 'Modern society with lift and security.', 'neighborhood': 'Ramdaspeth – shopping, schools, hospitals.', 'trends': 'Central location, steady rise.'},
    {'id': 9, 'title': 'Dharampeth Studio', 'location': 'Nagpur, Maharashtra', 'price': 6200000, 'bedrooms': 1, 'bathrooms': 1, 'area': 580, 'image': 'https://im.proptiger.com/1/672016/6/motif-images-for-elevation-of-universal-motif-739405.jpeg', 'description': 'Cozy studio for students or bachelors.', 'neighborhood': 'Dharampeth – colleges, cafes, markets.', 'trends': 'Student hub, 5% growth.'},

    # BANGALORE (3)
    {'id': 10, 'title': 'Whitefield Villa', 'location': 'Bangalore, Karnataka', 'price': 18500000, 'bedrooms': 4, 'bathrooms': 3, 'area': 2400, 'image': 'https://dyimg1.realestateindia.com/prop_images/2294416/1016528_1.jpg', 'description': 'Gated villa with private garden and clubhouse.', 'neighborhood': 'Whitefield – ITPL, Inorbit Mall, hospitals.', 'trends': 'IT boom, 10% YoY.'},
    {'id': 11, 'title': 'Indiranagar 3BHK', 'location': 'Bangalore, Karnataka', 'price': 22500000, 'bedrooms': 3, 'bathrooms': 2, 'area': 1600, 'image': 'https://thearchitectsdiary.com/wp-content/uploads/2017/12/IMGL2438-copy-Large.jpg', 'description': 'Premium flat in hip neighborhood.', 'neighborhood': 'Indiranagar – pubs, boutiques, metro.', 'trends': 'Lifestyle hub, 12% rise.'},
    {'id': 12, 'title': 'Koramangala Loft', 'location': 'Bangalore, Karnataka', 'price': 15500000, 'bedrooms': 2, 'bathrooms': 2, 'area': 1150, 'image': 'https://sankarassociates.in/wp-content/uploads/2020/05/1EXTERIOR-VIEW-300x200.jpg', 'description': 'Stylish loft with open layout.', 'neighborhood': 'Koramangala – startups, cafes, parks.', 'trends': 'Startup zone, 11% growth.'},

    # MYSORE (3)
    {'id': 13, 'title': 'Chamundi Hills Villa', 'location': 'Mysore, Karnataka', 'price': 17500000, 'bedrooms': 4, 'bathrooms': 3, 'area': 2300,'image': 'https://www.mytourplans.com/storage/ck/310523043907-glimpse-of-madhya-pradesh-with-chhattisgarh-tribal.jpg', 'description': 'Luxury villa with hill views and garden.', 'neighborhood': 'Near Chamundi Hills – temples, parks, schools.', 'trends': 'Tourist area, 7% appreciation.'},
    {'id': 14, 'title': 'VV Mohalla Flat', 'location': 'Mysore, Karnataka', 'price': 8800000, 'bedrooms': 2, 'bathrooms': 2, 'area': 1050, 'image': 'https://images.nigeriapropertycentre.com/properties/images/1524998/0636cbe4c8d90d-2bedroom-flat-prefinished-in-prime-location-block-of-flats-for-sale-life-camp-abuja.jpg', 'description': 'Comfortable family flat in calm area.', 'neighborhood': 'VV Mohalla – schools, hospitals, parks.', 'trends': 'Peaceful, 6% rise.'},
    {'id': 15, 'title': 'Heritage Studio', 'location': 'Mysore, Karnataka', 'price': 6200000, 'bedrooms': 1, 'bathrooms': 1, 'area': 620, 'image': 'https://static.toiimg.com/thumb/msid-82473938,width-748,height-499,resizemode=4,imgsize-1085388/Museum-of-Kerala-Arts-and-History-Kochi.jpg', 'description': 'Charming studio with traditional touch.', 'neighborhood': 'Near Chamundi Hills – yoga, nature.', 'trends': 'Spiritual hub, 5% growth.'},

    # MANGALORE (3)
    {'id': 16, 'title': 'Beachfront Villa', 'location': 'Mangalore, Karnataka', 'price': 21000000, 'bedrooms': 4, 'bathrooms': 3, 'area': 2200, 'image': 'https://media-cdn.tripadvisor.com/media/vr-splice-j/06/41/a4/32.jpg', 'description': 'Luxury villa with direct beach access.', 'neighborhood': 'Panambur Beach – seafood, ports, colleges.', 'trends': 'Coastal demand, 9% rise.'},
    {'id': 17, 'title': 'Kadri 3BHK', 'location': 'Mangalore, Karnataka', 'price': 11800000, 'bedrooms': 3, 'bathrooms': 2, 'area': 1400, 'image': 'https://gos3.ibcdn.com/dc3a8ac2-4a0a-4023-b39e-5666bf4d21ed.jpg', 'description': 'Modern apartment with sea breeze.', 'neighborhood': 'Kadri – malls, temples, hospitals.', 'trends': 'Growing city, 8% growth.'},
    {'id': 18, 'title': 'Bejai Studio', 'location': 'Mangalore, Karnataka', 'price': 7200000, 'bedrooms': 1, 'bathrooms': 1, 'area': 680, 'image': 'https://dyimg1.realestateindia.com/prop_images/3460366/1266571_1.jpeg', 'description': 'Compact studio near colleges.', 'neighborhood': 'Bejai – universities, hostels, cafes.', 'trends': 'Student area, 6% rise.'},

    # CHENNAI (3)
    {'id': 19, 'title': 'Anna Nagar Penthouse', 'location': 'Chennai, Tamil Nadu', 'price': 22000000, 'bedrooms': 3, 'bathrooms': 3, 'area': 1800, 'image': 'https://img.traveltriangle.com/blog/wp-content/uploads/2020/01/Coevr-for-Villas-in-Chennai_14th-jan.jpg', 'description': 'Rooftop terrace with city views.', 'neighborhood': 'Anna Nagar – metro, malls, schools.', 'trends': 'Central, 10% growth.'},
    {'id': 20, 'title': 'Adyar Sea View', 'location': 'Chennai, Tamil Nadu', 'price': 29500000, 'bedrooms': 4, 'bathrooms': 3, 'area': 2100, 'image': 'https://www.chennaidreamhomes.com/wp-content/uploads/2023/09/elevation2-1.jpg', 'description': 'Premium sea-facing apartment.', 'neighborhood': 'Adyar – Theosophical Society, beaches.', 'trends': 'Elite, 12% rise.'},
    {'id': 21, 'title': 'T Nagar Flat', 'location': 'Chennai, Tamil Nadu', 'price': 13800000, 'bedrooms': 2, 'bathrooms': 2, 'area': 1150, 'image': 'https://r1imghtlak.mmtcdn.com/98e9fcccf3b911ebb30f0a58a9feac02.jpg', 'description': 'Shopping paradise location.', 'neighborhood': 'T Nagar – silk sarees, markets, temples.', 'trends': 'Commercial hub, 9% growth.'},

    # COIMBATORE (3)
    {'id': 22, 'title': 'RS Puram Villa', 'location': 'Coimbatore, Tamil Nadu', 'price': 16800000, 'bedrooms': 4, 'bathrooms': 3, 'area': 2000, 'image': 'https://media-cdn.tripadvisor.com/media/photo-s/07/5d/49/94/cornerstay-serviced-apartment.jpg', 'description': 'Elegant villa in green area.', 'nehttps://media-cdn.tripadvisor.com/media/photo-s/08/3d/ca/d4/guest-room.jpgighborhood': 'RS Puram – hospitals, schools, malls.', 'trends': 'Industrial city, 8% rise.'},
    {'id': 23, 'title': 'Peelamedu 3BHK', 'location': 'Coimbatore, Tamil Nadu', 'price': 9800000, 'bedrooms': 3, 'bathrooms': 2, 'area': 1350, 'image': 'https://i.pinimg.com/originals/60/89/96/608996c5d86cfc8994d12ae87a06602f.jpg', 'description': 'Airport proximity flat.', 'neighborhood': 'Peelamedu – airport, IT parks.', 'trends': 'Aviation growth, 7% YoY.'},
    {'id': 24, 'title': 'Gandhipuram Studio', 'location': 'Coimbatore, Tamil Nadu', 'price': 6800000, 'bedrooms': 1, 'bathrooms': 1, 'area': 620, 'image': 'https://i.ytimg.com/vi/YgS9KHHUzRc/hqdefault.jpg', 'description': 'Central business district studio.', 'neighborhood': 'Gandhipuram – bus stand, markets.', 'trends': 'Commercial, 6% growth.'},

    # MADURAI (3)
    {'id': 25, 'title': 'Temple View Home', 'location': 'Madurai, Tamil Nadu', 'price': 11200000, 'bedrooms': 3, 'bathrooms': 2, 'area': 1600, 'image': 'https://a0.muscache.com/im/pictures/miso/Hosting-983908322379324081/original/db42e0f9-f900-4412-a6b2-4269abfe6c95.jpeg', 'description': 'Home with Meenakshi Temple view.', 'neighborhood': 'Near temple – culture, festivals.', 'trends': 'Heritage, 6% rise.'},
    {'id': 26, 'title': 'KK Nagar Flat', 'location': 'Madurai, Tamil Nadu', 'price': 7800000, 'bedrooms': 2, 'bathrooms': 2, 'area': 1050, 'image': 'https://housing-images.n7net.in/01c16c28/e96080acd4fedfa3559b390a46fa0191/v0/medium/3_bhk_independent_house-for-rent-vijayanagar_mysore-Mysore-others.jpg', 'description': 'Family-friendly society.', 'neighborhood': 'KK Nagar – schools, hospitals.', 'trends': 'Growing, 5% growth.'},
    {'id': 27, 'title': 'Anna Nagar Studio', 'location': 'Madurai, Tamil Nadu', 'price': 5500000, 'bedrooms': 1, 'bathrooms': 1, 'area': 580, 'image': 'https://images.nobroker.in/images/8a9f8b4392888da50192890474d007a4/8a9f8b4392888da50192890474d007a4_69447_474238_medium.jpg', 'description': 'Budget studio for students.', 'neighborhood': 'Near colleges – affordable living.', 'trends': 'Student demand, 4% rise.'},

    # AHMEDABAD (3)
    {'id': 28, 'title': 'SG Highway Villa', 'location': 'Ahmedabad, Gujarat', 'price': 19500000, 'bedrooms': 4, 'bathrooms': 3, 'area': 2300, 'image': 'https://files.propertywala.com/photos/9b/J721190032.main-entrance.1112987l.jpg', 'description': 'Modern villa on main highway.', 'neighborhood': 'SG Highway – malls, IT, hospitals.', 'trends': 'Business hub, 9% growth.'},
    {'id': 29, 'title': 'Satellite 3BHK', 'location': 'Ahmedabad, Gujarat', 'price': 12800000, 'bedrooms': 3, 'bathrooms': 2, 'area': 1450, 'image': 'https://dynamic.realestateindia.com/prop_images/225113/745064_1.jpg', 'description': 'Premium society flat.', 'neighborhood': 'Satellite – ISRO, schools, cafes.', 'trends': 'Upscale, 8% rise.'},
    {'id': 30, 'title': 'Navrangpura Studio', 'location': 'Ahmedabad, Gujarat', 'price': 7800000, 'bedrooms': 1, 'bathrooms': 1, 'area': 680, 'image': 'https://assets.architecturaldigest.in/photos/60083b47f93542952b6654fd/16:9/w_2560%2Cc_limit/ahmedabad-sudhir-bungalow-featured-image-1366x768.jpg', 'description': 'Central studio for professionals.', 'neighborhood': 'Navrangpura – universities, offices.', 'trends': 'Education hub, 7% growth.'},

    # SURAT (3)
    {'id': 31, 'title': 'Vesu Luxury Flat', 'location': 'Surat, Gujarat', 'price': 14200000, 'bedrooms': 3, 'bathrooms': 2, 'area': 1550, 'image': 'https://dyimg1.realestateindia.com/prop_images/3279675/1227984_5.jpg', 'description': 'High-rise luxury living.', 'neighborhood': 'Vesu – malls, diamond offices.', 'trends': 'Diamond city, 10% rise.'},
    {'id': 32, 'title': 'Adajan 2BHK', 'location': 'Surat, Gujarat', 'price': 8800000, 'bedrooms': 2, 'bathrooms': 2, 'area': 1100, 'image': 'https://5.imimg.com/data5/OS/OF/MY-13018244/drawing-25-500x500.jpg', 'description': 'Family flat in growing area.', 'neighborhood': 'Adajan – schools, hospitals.', 'trends': 'Expanding, 8% growth.'},
    {'id': 33, 'title': 'Pal Studio', 'location': 'Surat, Gujarat', 'price': 6200000, 'bedrooms': 1, 'bathrooms': 1, 'area': 620, 'image': 'https://5.imimg.com/data5/SELLER/Default/2022/10/UL/TV/DN/160529616/4-bhk-row-houses-500x500.jpg', 'description': 'Affordable studio for bachelors.', 'neighborhood': 'Pal – textile markets, food.', 'trends': 'Commercial, 6% rise.'},

    # VADODARA (3)
    {'id': 34, 'title': 'Alkapuri Bungalow', 'location': 'Vadodara, Gujarat', 'price': 16800000, 'bedrooms': 4, 'bathrooms': 3, 'area': 2100, 'image': 'https://i.pinimg.com/736x/f2/54/06/f25406c8be49f8ee396dec4d4ade4d15.jpg', 'description': 'Classic bungalow in elite area.', 'neighborhood': 'Alkapuri – malls, clubs, offices.', 'trends': 'Heritage, 7% growth.'},
    {'id': 35, 'title': 'Gotri 3BHK', 'location': 'Vadodara, Gujarat', 'price': 9800000, 'bedrooms': 3, 'bathrooms': 2, 'area': 1350, 'image': 'https://housing-images.n7net.in/01c16c28/09b36f1aec4b0873be17b734e8ab2f79/v0/large/3_bhk_apartment-for-sale-gotri-Vadodara-hall.jpg', 'description': 'Modern flat in green zone.', 'neighborhood': 'Gotri – hospitals, schools.', 'trends': 'Family area, 6% rise.'},
    {'id': 36, 'title': 'Akota Studio', 'location': 'Vadodara, Gujarat', 'price': 6800000, 'bedrooms': 1, 'bathrooms': 1, 'area': 620, 'image': 'https://www.a2zproperty.in/Gujarat/Vadodara/aashrith/image-1592-6.jpg', 'description': 'Compact studio near river.', 'neighborhood': 'Akota – gardens, cafes.', 'trends': 'Scenic, 5% growth.'},

    # JAIPUR (3)
    {'id': 37, 'title': 'C-Scheme Villa', 'location': 'Jaipur, Rajasthan', 'price': 18500000, 'bedrooms': 4, 'bathrooms': 3, 'area': 2200, 'image': 'https://a0.muscache.com/im/pictures/miso/Hosting-38910518/original/7dec68a0-ad52-497d-bf57-0dd5fc78f9e7.jpeg', 'description': 'Royal-style villa with courtyard.', 'neighborhood': 'C-Scheme – Raj Mandir, cafes.', 'trends': 'Tourism, 8% rise.'},
    {'id': 38, 'title': 'Malviya Nagar Flat', 'location': 'Jaipur, Rajasthan', 'price': 11200000, 'bedrooms': 3, 'bathrooms': 2, 'area': 1350, 'image': 'https://img.staticmb.com/mbimages/project/Photo_h300_w450/Project-Photo-14-Pomposh-Jaipur-5102765_564_800_300_450.jpg', 'description': 'Modern flat near airport.', 'neighborhood': 'Malviya Nagar – malls, schools.', 'trends': 'Growing, 7% growth.'},
    {'id': 39, 'title': 'Vaishali Nagar Studio', 'location': 'Jaipur, Rajasthan', 'price': 7200000, 'bedrooms': 1, 'bathrooms': 1, 'area': 620, 'image': 'https://im.proptiger.com/1/3243685/6/barjswer-homers-2-elevation-147351820.jpeg', 'description': 'Budget studio for students.', 'neighborhood': 'Vaishali Nagar – colleges, food.', 'trends': 'Education, 6% rise.'},

    # UDAIPUR (3)
    {'id': 40, 'title': 'Lake View Villa', 'location': 'Udaipur, Rajasthan', 'price': 22500000, 'bedrooms': 4, 'bathrooms': 3, 'area': 2400, 'image': 'https://img.vistarooms.com/gallery/compressed/ikebana-50ffd6.jpg', 'description': 'Palace-like villa with lake view.', 'neighborhood': 'Near Lake Pichola – boats, hotels.', 'trends': 'Luxury tourism, 12% rise.'},
    {'id': 41, 'title': 'Hiran Magri 3BHK', 'location': 'Udaipur, Rajasthan', 'price': 9800000, 'bedrooms': 3, 'bathrooms': 2, 'area': 1350, 'image': 'https://newprojects.99acres.com/projects/siddhatva_enclave_private_limited/siddhatva_skyline/images/hx4zkyy_1717069271_495313832_large.jpg', 'description': 'Family flat in calm area.', 'neighborhood': 'Hiran Magri – schools, markets.', 'trends': 'Peaceful, 6% growth.'},
    {'id': 42, 'title': 'Fatehpura Studio', 'location': 'Udaipur, Rajasthan', 'price': 6800000, 'bedrooms': 1, 'bathrooms': 1, 'area': 620, 'image': 'https://www.mountainhomes.in/img/gallery/5.jpg', 'description': 'Lake-facing studio.', 'neighborhood': 'Fatehpura – cafes, views.', 'trends': 'Scenic, 5% rise.'},

    # JODHPUR (3)
    {'id': 43, 'title': 'Sardarpura Bungalow', 'location': 'Jodhpur, Rajasthan', 'price': 15800000, 'bedrooms': 4, 'bathrooms': 3, 'area': 2000, 'image': 'https://a0.muscache.com/im/pictures/211db20f-c26c-4b05-99ad-52e5e938b14f.jpg', 'description': 'Blue city charm bungalow.', 'neighborhood': 'Sardarpura – markets, forts.', 'trends': 'Heritage, 7% growth.'},
    {'id': 44, 'title': 'Paota 3BHK', 'location': 'Jodhpur, Rajasthan', 'price': 9200000, 'bedrooms': 3, 'bathrooms': 2, 'area': 1250, 'image': 'https://dynamic.realestateindia.com/prop_images/1358261/765399_5.jpg', 'description': 'Modern flat in old city.', 'neighborhood': 'Paota – clock tower, food.', 'trends': 'Central, 6% rise.'},
    {'id': 45, 'title': 'Shastri Nagar Studio', 'location': 'Jodhpur, Rajasthan', 'price': 6200000, 'bedrooms': 1, 'bathrooms': 1, 'area': 580, 'image': 'https://ashapurna.com/blog/wp-content/uploads/2022/08/WhatsApp-Image-2022-08-20-at-6.43.29-PM-2-640x482.jpeg', 'description': 'Compact studio for travelers.', 'neighborhood': 'Shastri Nagar – hostels, cafes.', 'trends': 'Tourist area, 5% growth.'},
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        state = request.form.get('state', '')
        city = request.form.get('city', '')
        price_range = request.form.get('price_range', '')

        min_price, max_price = 0, float('inf')
        if price_range and '-' in price_range:
            min_str, max_str = price_range.split('-')
            min_price = int(min_str)
            max_price = int(max_str)
        elif price_range and int(price_range.split('-')[0]) >= 50000000:
            min_price = 50000000

        filtered = [
            p for p in properties
            if (not state or state in p['location']) and
               (not city or city in p['location']) and
               min_price <= p['price'] <= max_price
        ]
        return render_template('results.html', properties=filtered)

    return render_template('index.html')

@app.route('/property/<int:prop_id>')
def property_detail(prop_id):
    prop = next((p for p in properties if p['id'] == prop_id), None)
    if prop:
        return render_template('detail.html', property=prop)
    return 'Property not found', 404

if __name__ == '__main__':
    app.run(debug=True)