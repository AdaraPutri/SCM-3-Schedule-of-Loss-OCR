from dataclasses import dataclass, field
from datetime import date
from decimal import Decimal
from enum import Enum
from typing import Optional


class Category(str, Enum):
    UNCATEGORIZED = "Uncategorized"
    BUILDING = "Building"
    CONTENTS = "Contents"
    ALE = "ALE"
  
# Represents an individual line item on a receipt  
@dataclass
class LineItem:
    description: str
    price: Optional[Decimal]
    category: Category = Category.UNCATEGORIZED
    
@dataclass
class Receipt:
    vendor: str
    purchase_date: Optional[date]
    items: list[LineItem] = field(default_factory=list)
    total: Optional[Decimal] = None
    tip: Optional[Decimal] = None
    use_total: bool = False # Whether to do extract per item or per receipt. True is per receipt
    category: Category = Category.UNCATEGORIZED
    image_name: Optional[str] = None
    
# Represents a row that has complete fields and is ready to be added to SOL
@dataclass
class SheetRow:
    description: str
    vendor: str
    purchase_date: Optional[date]
    category: Category
    price: Optional[Decimal]
    tip: Optional[Decimal]
    
@dataclass
class ScannedReceipt:
    receipt: Receipt
    image: bytes
    