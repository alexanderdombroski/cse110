class ClassName {
    // Attributes:
    private string _name;
    private int _stock;
    private float _price;
    
    // Constructors:
    public ClassName(string name, float price, int stock=0) {
        _name = name;
        _price = price;
        _stock = stock;
    }

    // Methods:
    public void add_stock(int stockQuantity) {
        _stock += stockQuantity
    }
}

