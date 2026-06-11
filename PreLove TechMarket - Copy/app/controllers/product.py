from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models.product import Product

product_bp = Blueprint('product', __name__)

#Home
@product_bp.route('/')
def home():
    featured_products = Product.query.filter(Product.tag != 'SALE').limit(10).all()
    sale_products = Product.query.filter_by(tag='SALE').all()

    categories = [
        {"name": "Dresses",   "icon": "👗"},
        {"name": "Tops",      "icon": "👚"},
        {"name": "Pants",     "icon": "👖"},
        {"name": "Swim Wear", "icon": "👙"},
        {"name": "Jacket",    "icon": "🥼"},
        {"name": "Shorts",    "icon": "🩳"},
    ]

    # sale_products = [
    #     {"name": "Gray Top",        "image": "img/Tops/Onsale_TOPS.jpg",        "old_price": 60, "price": 45},
    #     {"name": "Denim Dress",     "image": "img/Dresses/onsale_dress.jpg",     "old_price": 60, "price": 45},
    #     {"name": "Stylish Jacket",  "image": "img/Jackets/onsale_jackets.jpg",   "old_price": 60, "price": 45},
    #     {"name": "Pants",           "image": "img/Pants/onsale_pants.jpg",       "old_price": 60, "price": 45},
    #     {"name": "Gathered Skirt",  "image": "img/Shorts/onsale_shorts.jpg",     "old_price": 60, "price": 45},
    #     {"name": "Black One Piece", "image": "img/Swimwear/onsale_Swimwear.jpg", "old_price": 60, "price": 45},
    # ]

    features = [
        {"icon": "fa-solid fa-truck-fast fa-beat-fade",        "title": "Free shipping & return", "desc": "Free shipping on all PH orders"},
        {"icon": "fa-sharp fa-solid fa-peso-sign fa-beat-fade","title": "Money Guarantee",        "desc": "Secure transactions 24/7"},
        {"icon": "fa-solid fa-headset fa-bounce",              "title": "Online Support",         "desc": "We support online 24/7"},
        {"icon": "fa-solid fa-credit-card fa-beat-fade",       "title": "Secure Payments",        "desc": "Payment is Secured & trusted"},
    ]

    reviews = [
        {"text": "Grabe, hindi halatang preloved! Akala ko brand new yung dumating kasi sobrang bango at mukhang hindi pa gamit. Sobrang sulit ng bayad ko rito kaysa bumili sa mall.💖 #BudolIsReal", "stars": "⭐⭐⭐⭐⭐", "name": "Carms"},
        {"text": "Ang ganda ng curation ni seller! Pang-IG yung mga damit at saktong-sakto yung fit sa akin. Mabilis din napa-ship kaya nagamit ko agad sa gala namin. ✨👗", "stars": "⭐⭐⭐⭐⭐", "name": "Aya"},
        {"text": "First time ko bumili rito at hindi ako nabigo. Very responsive si seller sa mga questions ko about measurements. Honest din siya sa condition ng damit. #💸💸💸", "stars": "⭐⭐⭐⭐⭐", "name": "Janine"},
        {"text": "Solid 'to. Akala ko kupas na kasi preloved, pero mukhang bago pa talaga. Sakto yung fit, hindi tipid sa tela. Sulit ang bayad dito kaysa bumili sa mall. 🔥", "stars": "⭐⭐⭐⭐⭐", "name": "Jm"},
        {"text": "Eto yung hinahanap kong porma na hindi masakit sa bulsa. Ayos yung curation ni seller, pang-porma talaga. Nakuha ko agad bago yung lakad namin ng tropa.", "stars": "⭐⭐⭐⭐⭐", "name": "Bedict"},
    ]

    return render_template('public/home.html',
        featured_products=featured_products,
        categories=categories,
        sale_products=sale_products,
        features=features,
        reviews=reviews
    )

@product_bp.route('/Shop')
def shop():
    products = Product.query.all()
    return render_template('public/shop.html', products=products)

#Admin
@product_bp.route('/Admin')
def all_products():
    all_products = Product.query.all()
    return render_template('public/product/all_products.html', all_products=all_products) 

#productdeatail
@product_bp.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get(product_id)
    if product is None:
        flash('Product not found.', 'error')
        return redirect(url_for('product.shop'))
    all_products = Product.query.all()
    return render_template('public/product_detail.html', product=product,all_products=all_products)

#CREATEadd
@product_bp.route('/product/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name      = request.form.get('name')
        desc      = request.form.get('desc')
        price     = request.form.get('price')
        old_price = request.form.get('old_price') or None 
        condition = request.form.get('condition')
        image     = request.form.get('image')
        tag       = request.form.get('tag')
        category  = request.form.get('category')

        if not name or not price:
            flash('Name and price are required.', 'error')
            return redirect(url_for('product.add_product'))

        new_product = Product(
            name=name, desc=desc, price=price, old_price = old_price,
            condition=condition, image=image,
            tag=tag, category=category
        )
        db.session.add(new_product)
        db.session.commit()
        flash('Product added successfully!', 'success')
        return redirect(url_for('product.shop'))

    return render_template('public/product/add_product.html')

#update
@product_bp.route('/product/<int:product_id>/edit', methods=['GET', 'POST'])
def edit_product(product_id):
    product = Product.query.get(product_id)
    if product is None:
        flash('Product not found.', 'error')
        return redirect(url_for('product.shop'))

    if request.method == 'POST':
        name  = request.form.get('name')
        price = request.form.get('price')

        if not name or not price:
            flash('Name and price are required.', 'error')
            return redirect(url_for('product.edit_product', product_id=product_id))

        product.name      = name
        product.desc      = request.form.get('desc')
        product.price     = price
        product.condition = request.form.get('condition')
        product.image     = request.form.get('image')
        product.tag       = request.form.get('tag')
        product.old_price = request.form.get('old_price') or None
        product.category  = request.form.get('category')
        db.session.commit()
        flash('Product updated successfully!', 'success')
        return redirect(url_for('product.product_detail', product_id=product.id))

    return render_template('public/product/edit_product.html', product=product)

#delete
@product_bp.route('/product/<int:product_id>/delete', methods=['GET', 'POST'])
def delete_product(product_id):
    product = Product.query.get(product_id)
    if product is None:
        flash('Product not found.', 'error')
        return redirect(url_for('product.shop'))

    if request.method == 'POST':
        db.session.delete(product)
        db.session.commit()
        flash(f'{product.name} has been deleted.', 'success')
        return redirect(url_for('product.shop'))

    return render_template('public/product/confirm_delete.html', product=product)