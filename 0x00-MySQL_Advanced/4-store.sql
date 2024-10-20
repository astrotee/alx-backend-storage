-- Buy buy buy
-- update quantities agfter orders
CREATE TRIGGER qnt_upd AFTER INSERT ON orders
FOR EACH ROW
UPDATE items
  SET quantity = quantity - NEW.number
  WHERE name = NEW.item_name;;
