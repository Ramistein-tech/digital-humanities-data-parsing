#!/usr/bin/env python3
"""
XML/TEI Historical Data Extractor
Author: Rami Izzeddin
"""

import xml.etree.ElementTree as ET

def parse_sample_xml():
    """Simulate parsing structured text nodes from an XML string."""
    raw_xml = """<tei>
        <header><title>Archaeological Record</title></header>
        <text><body><p>Sample historical inscription text.</p></body></text>
    </tei>"""
    
    root = ET.fromstring(raw_xml)
    title = root.find(".//title").text
    body = root.find(".//p").text
    
    print(f"Dataset Title: {title}")
    print(f"Extracted Body: {body}")

if __name__ == "__main__":
    parse_sample_xml()
