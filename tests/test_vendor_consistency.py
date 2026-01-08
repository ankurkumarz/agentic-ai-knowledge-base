#!/usr/bin/env python3
"""
Property-based tests for vendor section consistency.

**Feature: knowledge-base-reorganization, Property 8: Vendor Section Consistency**
**Validates: Requirements 5.3, 5.4**

This test validates that all vendor ecosystem sections maintain consistent
structure including platform overviews, tools, APIs, and integration patterns.
"""

import os
import re
from pathlib import Path
from hypothesis import given, strategies as st, assume
from hypothesis import settings, HealthCheck
import pytest


class TestVendorSectionConsistency:
    """Property-based tests for vendor section consistency validation."""
    
    @classmethod
    def setup_class(cls):
        """Set up test environment."""
        cls.project_root = Path(__file__).parent.parent
        cls.docs_dir = cls.project_root / "docs"
        cls.vendor_dirs = [
            "AllThingsAWS",
            "AllThingsGoogle", 
            "AllThingsMicrosoft",
            "AllThingsAnthropic",
            "AllThingsOpenAI"
        ]
        
    def test_all_vendor_directories_exist(self):
        """Test that all required vendor directories exist."""
        for vendor_dir in self.vendor_dirs:
            vendor_path = self.docs_dir / vendor_dir
            assert vendor_path.exists(), f"Vendor directory '{vendor_dir}' must exist"
            assert vendor_path.is_dir(), f"'{vendor_dir}' must be a directory"
            
    def test_all_vendor_readmes_exist(self):
        """Test that all vendor directories have README.md files."""
        for vendor_dir in self.vendor_dirs:
            readme_path = self.docs_dir / vendor_dir / "README.md"
            assert readme_path.exists(), f"README.md must exist in '{vendor_dir}'"
            assert readme_path.is_file(), f"README.md in '{vendor_dir}' must be a file"
            
    def test_vendor_readme_content_structure(self):
        """Test that vendor README files have consistent structure."""
        required_sections = [
            "platform",  # Platform overview content
            "tool",       # Tools/SDKs information  
            "api",        # API capabilities
            "integration" # Integration patterns
        ]
        
        for vendor_dir in self.vendor_dirs:
            readme_path = self.docs_dir / vendor_dir / "README.md"
            
            with open(readme_path, 'r', encoding='utf-8') as f:
                content = f.read().lower()
                
            # Check that content contains references to required concepts
            for section_keyword in required_sections:
                assert section_keyword in content, \
                    f"'{vendor_dir}/README.md' must contain '{section_keyword}' related content"
                    
    def test_vendor_naming_convention_consistency(self):
        """Test that all vendor directories follow the AllThings* naming pattern."""
        for vendor_dir in self.vendor_dirs:
            assert vendor_dir.startswith("AllThings"), \
                f"Vendor directory '{vendor_dir}' must start with 'AllThings'"
            assert len(vendor_dir) > len("AllThings"), \
                f"Vendor directory '{vendor_dir}' must have vendor name after 'AllThings'"
                
    @given(st.sampled_from([
        "AllThingsAWS", "AllThingsGoogle", "AllThingsMicrosoft", 
        "AllThingsAnthropic", "AllThingsOpenAI"
    ]))
    @settings(suppress_health_check=[HealthCheck.function_scoped_fixture])
    def test_vendor_section_consistency_property(self, vendor_dir):
        """
        Property test: For any vendor ecosystem section, it should maintain 
        consistent structure including platform overviews, tools, APIs, and 
        integration patterns.
        
        **Property 8: Vendor Section Consistency**
        **Validates: Requirements 5.3, 5.4**
        """
        readme_path = self.docs_dir / vendor_dir / "README.md"
        
        # Ensure the vendor directory and README exist
        assert readme_path.exists(), f"README.md must exist for {vendor_dir}"
        
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Test that content is substantial (not just a placeholder)
        assert len(content.strip()) > 100, \
            f"'{vendor_dir}/README.md' must contain substantial content"
            
        # Test that content has proper markdown structure
        assert content.startswith('#'), \
            f"'{vendor_dir}/README.md' must start with a markdown header"
            
        # Test for consistent structural elements across vendors
        content_lower = content.lower()
        
        # Should contain platform/ecosystem information
        platform_indicators = ['platform', 'ecosystem', 'service', 'cloud']
        assert any(indicator in content_lower for indicator in platform_indicators), \
            f"'{vendor_dir}/README.md' must contain platform/ecosystem information"
            
        # Should contain tools/SDK information  
        tools_indicators = ['tool', 'sdk', 'api', 'library', 'framework']
        assert any(indicator in content_lower for indicator in tools_indicators), \
            f"'{vendor_dir}/README.md' must contain tools/SDK information"
            
        # Should contain links or references (indicating comprehensive coverage)
        link_indicators = ['http', 'github', 'docs', 'documentation']
        assert any(indicator in content_lower for indicator in link_indicators), \
            f"'{vendor_dir}/README.md' must contain external references/links"
            
        # Test markdown formatting consistency
        headers = re.findall(r'^#+\s+(.+)$', content, re.MULTILINE)
        assert len(headers) >= 2, \
            f"'{vendor_dir}/README.md' must have at least 2 section headers"
            
        # Test that content is organized (has multiple sections)
        sections = content.split('\n## ')
        assert len(sections) >= 2, \
            f"'{vendor_dir}/README.md' must have multiple organized sections"
            
    def test_vendor_content_uniqueness(self):
        """Test that each vendor section has unique, vendor-specific content."""
        vendor_contents = {}
        
        for vendor_dir in self.vendor_dirs:
            readme_path = self.docs_dir / vendor_dir / "README.md"
            
            with open(readme_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            vendor_contents[vendor_dir] = content
            
        # Test that vendor sections are not identical (each has unique content)
        vendor_names = list(vendor_contents.keys())
        for i, vendor1 in enumerate(vendor_names):
            for vendor2 in vendor_names[i+1:]:
                content1 = vendor_contents[vendor1].lower()
                content2 = vendor_contents[vendor2].lower()
                
                # Calculate simple similarity (shared words)
                words1 = set(content1.split())
                words2 = set(content2.split())
                
                if len(words1) > 0 and len(words2) > 0:
                    similarity = len(words1.intersection(words2)) / len(words1.union(words2))
                    
                    # Content should not be too similar (allowing for some common terms)
                    assert similarity < 0.8, \
                        f"'{vendor1}' and '{vendor2}' content is too similar - each should have unique vendor-specific content"
                        
    def test_vendor_section_completeness(self):
        """Test that vendor sections provide comprehensive coverage."""
        for vendor_dir in self.vendor_dirs:
            readme_path = self.docs_dir / vendor_dir / "README.md"
            
            with open(readme_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            content_lower = content.lower()
            
            # Extract vendor name from directory
            vendor_name = vendor_dir.replace("AllThings", "").lower()
            
            # Should mention the vendor name prominently
            assert vendor_name in content_lower, \
                f"'{vendor_dir}/README.md' must prominently mention '{vendor_name}'"
                
            # Should have substantial content (comprehensive coverage)
            word_count = len(content.split())
            assert word_count >= 200, \
                f"'{vendor_dir}/README.md' should have comprehensive content (at least 200 words, found {word_count})"
                
            # Should have multiple sections for comprehensive coverage
            section_count = len(re.findall(r'^##\s+', content, re.MULTILINE))
            assert section_count >= 3, \
                f"'{vendor_dir}/README.md' should have at least 3 main sections for comprehensive coverage"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])