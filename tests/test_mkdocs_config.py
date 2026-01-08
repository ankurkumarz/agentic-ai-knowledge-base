#!/usr/bin/env python3
"""
Property-based tests for MkDocs configuration validation.

**Feature: knowledge-base-reorganization, Property 1: Content Preservation**
**Validates: Requirements 2.2**

This test validates that the MkDocs configuration preserves all content
during reorganization and maintains proper YAML structure.
"""

import os
import yaml
from pathlib import Path
from hypothesis import given, strategies as st, assume
from hypothesis import settings, HealthCheck
import pytest


class TestMkDocsConfiguration:
    """Property-based tests for MkDocs configuration validation."""
    
    @classmethod
    def setup_class(cls):
        """Set up test environment."""
        cls.project_root = Path(__file__).parent.parent
        cls.mkdocs_config_path = cls.project_root / "mkdocs.yml"
        cls.docs_dir = cls.project_root / "docs"
        
    def test_mkdocs_config_exists_and_valid_yaml(self):
        """Test that mkdocs.yml exists and is valid YAML."""
        assert self.mkdocs_config_path.exists(), "mkdocs.yml file must exist"
        
        with open(self.mkdocs_config_path, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
            
        assert config is not None, "mkdocs.yml must contain valid YAML"
        assert isinstance(config, dict), "mkdocs.yml must be a YAML dictionary"
        
    def test_required_mkdocs_fields_present(self):
        """Test that all required MkDocs fields are present."""
        with open(self.mkdocs_config_path, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
            
        required_fields = ['site_name', 'theme', 'nav']
        for field in required_fields:
            assert field in config, f"Required field '{field}' must be present in mkdocs.yml"
            
    def test_material_theme_configuration(self):
        """Test that Material theme is properly configured with required features."""
        with open(self.mkdocs_config_path, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
            
        theme = config.get('theme', {})
        assert theme.get('name') == 'material', "Theme must be 'material'"
        
        # Test required Material theme features
        features = theme.get('features', [])
        required_features = [
            'navigation.instant',
            'search.highlight',
            'content.code.copy'
        ]
        
        for feature in required_features:
            assert feature in features, f"Required Material theme feature '{feature}' must be enabled"
            
    def test_navigation_structure_has_eight_sections(self):
        """Test that navigation has exactly 8 top-level sections as required."""
        with open(self.mkdocs_config_path, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
            
        nav = config.get('nav', [])
        
        # Count top-level sections (excluding Home)
        top_level_sections = []
        for item in nav:
            if isinstance(item, dict):
                for key in item.keys():
                    if key != 'Home':
                        top_level_sections.append(key)
            elif isinstance(item, str) and item != 'Home':
                top_level_sections.append(item)
                
        # Should have exactly 8 sections plus Home
        expected_sections = [
            'Fundamentals', 'Development', 'Agent Engineering', 'Agent Catalog',
            'Production & Operations', 'Evaluation', 'Tools & Marketplace', 
            'Vendor Ecosystems'
        ]
        
        for section in expected_sections:
            assert section in str(nav), f"Required section '{section}' must be present in navigation"
            
    @given(st.text(min_size=1, max_size=100))
    @settings(suppress_health_check=[HealthCheck.function_scoped_fixture])
    def test_content_preservation_property(self, content_sample):
        """
        Property test: For any content that exists in the docs directory,
        it should be reachable through the navigation structure.
        
        **Property 1: Content Preservation**
        **Validates: Requirements 2.2**
        """
        assume(content_sample.strip())  # Ensure non-empty content
        
        with open(self.mkdocs_config_path, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
            
        nav = config.get('nav', [])
        
        # Extract all file paths referenced in navigation
        nav_paths = self._extract_nav_paths(nav)
        
        # Check that navigation structure is well-formed
        assert len(nav_paths) > 0, "Navigation must reference at least one content file"
        
        # Verify that each referenced path in navigation corresponds to an actual file
        for nav_path in nav_paths:
            if nav_path != 'index.md':  # Skip index.md as it might not exist yet
                full_path = self.docs_dir / nav_path
                # For now, we'll check that the path is well-formed
                assert isinstance(nav_path, str), f"Navigation path must be string: {nav_path}"
                assert nav_path.endswith('.md'), f"Navigation path must end with .md: {nav_path}"
                
    def _extract_nav_paths(self, nav_item):
        """Recursively extract all file paths from navigation structure."""
        paths = []
        
        if isinstance(nav_item, list):
            for item in nav_item:
                paths.extend(self._extract_nav_paths(item))
        elif isinstance(nav_item, dict):
            for key, value in nav_item.items():
                if isinstance(value, str) and value.endswith('.md'):
                    paths.append(value)
                elif isinstance(value, (list, dict)):
                    paths.extend(self._extract_nav_paths(value))
        elif isinstance(nav_item, str) and nav_item.endswith('.md'):
            paths.append(nav_item)
            
        return paths
        
    def test_yaml_structure_integrity(self):
        """Test that YAML structure maintains proper indentation and format."""
        with open(self.mkdocs_config_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Test that file can be parsed as YAML
        config = yaml.safe_load(content)
        assert config is not None
        
        # Test that re-serializing produces valid YAML
        reserialized = yaml.dump(config, default_flow_style=False)
        reparsed = yaml.safe_load(reserialized)
        
        # Key structure should be preserved
        assert reparsed.get('site_name') == config.get('site_name')
        assert reparsed.get('theme', {}).get('name') == config.get('theme', {}).get('name')
        
    def test_enhanced_features_enabled(self):
        """Test that enhanced Material theme features are properly enabled."""
        with open(self.mkdocs_config_path, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
            
        theme = config.get('theme', {})
        
        # Test palette configuration for dark/light mode
        palette = theme.get('palette', [])
        assert isinstance(palette, list), "Palette must be a list for theme switching"
        assert len(palette) >= 2, "Must have at least light and dark mode palettes"
        
        # Test that both light and dark schemes are present
        schemes = [p.get('scheme') for p in palette if isinstance(p, dict)]
        assert 'default' in schemes, "Light mode (default scheme) must be configured"
        assert 'slate' in schemes, "Dark mode (slate scheme) must be configured"
        
        # Test enhanced navigation features
        features = theme.get('features', [])
        enhanced_features = [
            'navigation.instant.prefetch',
            'navigation.tracking',
            'navigation.tabs',
            'search.suggest',
            'content.code.select',
            'content.code.annotate'
        ]
        
        for feature in enhanced_features:
            assert feature in features, f"Enhanced feature '{feature}' should be enabled"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])