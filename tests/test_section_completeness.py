#!/usr/bin/env python3
"""
Property-based tests for section completeness validation.

**Feature: knowledge-base-reorganization, Property 5: Content Consolidation Without Loss**
**Validates: Requirements 2.2**

This test validates that content reorganization preserves all existing information
without data loss during the consolidation process.
"""

import os
import re
from pathlib import Path
from hypothesis import given, strategies as st, assume
from hypothesis import settings, HealthCheck
import pytest
import yaml


class TestSectionCompleteness:
    """Property-based tests for section completeness validation."""
    
    @classmethod
    def setup_class(cls):
        """Set up test environment."""
        cls.project_root = Path(__file__).parent.parent
        cls.docs_dir = cls.project_root / "docs"
        cls.mkdocs_config_path = cls.project_root / "mkdocs.yml"
        
        # Define the current folder structure that should be preserved
        cls.current_folders = [
            "AgentMemory", "AgentPlatforms", "AgentReferenceArch", "AgenticFrameworks",
            "AgenticTechStack", "AllThingsAWS", "AllThingsAnthropic", "AllThingsGoogle",
            "AllThingsMicrosoft", "AllThingsOpenAI", "ArchitectureDesignPatterns",
            "Benchmarks", "BestPractices", "Caching", "CloudHosting", "CodeExamples",
            "CodeSandbox", "Concepts", "ContextEngineeeing", "Courses", "DesignPatterns",
            "DevAgents", "EvaluationFrameworks", "Foundations", "Gartner", "Introduction",
            "LLM", "LLMGateway", "MCP", "Marketplace", "MaturityModels", "NewsletterBlogs",
            "Observability", "PromptEngineering", "PromptRepository", "RAG",
            "ReferenceArchitecture", "Research", "ResearchAgents", "Resiliency",
            "RetrievalApproaches", "SaaSPlatforms", "SampleApps", "SecurityFrameworks",
            "Standards", "WebSearchCrawl", "WorkflowBuilders"
        ]
        
    def test_all_current_folders_exist(self):
        """Test that all current documentation folders still exist."""
        for folder_name in self.current_folders:
            folder_path = self.docs_dir / folder_name
            assert folder_path.exists(), f"Folder '{folder_name}' must still exist in docs directory"
            assert folder_path.is_dir(), f"'{folder_name}' must be a directory"
            
    def test_all_readme_files_preserved(self):
        """Test that all README.md files are preserved in current folders."""
        for folder_name in self.current_folders:
            readme_path = self.docs_dir / folder_name / "README.md"
            if readme_path.exists():
                assert readme_path.is_file(), f"README.md in '{folder_name}' must be a file"
                
                # Verify file has content
                with open(readme_path, 'r', encoding='utf-8') as f:
                    content = f.read().strip()
                    assert len(content) > 0, f"README.md in '{folder_name}' must not be empty"
                    
    def test_content_file_preservation(self):
        """Test that all content files are preserved during reorganization."""
        total_files_found = 0
        
        for folder_name in self.current_folders:
            folder_path = self.docs_dir / folder_name
            if folder_path.exists():
                # Count all markdown files in the folder
                md_files = list(folder_path.glob("*.md"))
                total_files_found += len(md_files)
                
                # Verify each markdown file has content
                for md_file in md_files:
                    with open(md_file, 'r', encoding='utf-8') as f:
                        content = f.read().strip()
                        assert len(content) > 0, f"Content file '{md_file}' must not be empty"
                        
        # Should have found substantial content across all folders
        assert total_files_found >= 40, f"Should preserve substantial content files (found {total_files_found})"
        
    @given(st.sampled_from([
        "AgentMemory", "AgentPlatforms", "AgenticFrameworks", "AllThingsAWS",
        "AllThingsGoogle", "BestPractices", "Concepts", "DesignPatterns",
        "EvaluationFrameworks", "Foundations", "LLM", "MCP", "Observability",
        "PromptEngineering", "RAG", "SecurityFrameworks", "Standards"
    ]))
    @settings(suppress_health_check=[HealthCheck.function_scoped_fixture])
    def test_content_consolidation_without_loss_property(self, folder_name):
        """
        Property test: For any content reorganization operation, all original 
        information should be preserved and accessible in the new structure.
        
        **Property 5: Content Consolidation Without Loss**
        **Validates: Requirements 2.2**
        """
        folder_path = self.docs_dir / folder_name
        
        # Ensure the folder exists (content preservation)
        assert folder_path.exists(), f"Folder '{folder_name}' must be preserved during reorganization"
        
        # Check for README.md file
        readme_path = folder_path / "README.md"
        if readme_path.exists():
            with open(readme_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Content must be substantial (not just placeholder)
            assert len(content.strip()) > 50, \
                f"Content in '{folder_name}/README.md' must be substantial and preserved"
                
            # Content must have proper markdown structure
            assert content.strip().startswith('#'), \
                f"Content in '{folder_name}/README.md' must maintain proper markdown structure"
                
            # Content should contain meaningful information (not just boilerplate)
            content_lower = content.lower()
            meaningful_indicators = [
                'agent', 'ai', 'framework', 'platform', 'tool', 'service',
                'architecture', 'design', 'pattern', 'implementation', 'api',
                'sdk', 'library', 'model', 'llm', 'evaluation', 'security',
                'observability', 'memory', 'context', 'prompt', 'rag'
            ]
            
            has_meaningful_content = any(indicator in content_lower for indicator in meaningful_indicators)
            assert has_meaningful_content, \
                f"Content in '{folder_name}/README.md' must contain meaningful domain-specific information"
                
        # Check that folder contains expected file types
        all_files = list(folder_path.glob("*"))
        file_extensions = [f.suffix for f in all_files if f.is_file()]
        
        # Should contain markdown files or other documentation formats
        expected_extensions = ['.md', '.txt', '.rst', '.png', '.jpg', '.jpeg', '.svg']
        has_documentation = any(ext in file_extensions for ext in expected_extensions)
        
        if len(all_files) > 0:  # Only check if folder has files
            assert has_documentation, \
                f"Folder '{folder_name}' must contain documentation files with expected extensions"
                
    def test_navigation_references_preserved_content(self):
        """Test that navigation structure references preserved content appropriately."""
        if not self.mkdocs_config_path.exists():
            pytest.skip("mkdocs.yml not found - skipping navigation test")
            
        with open(self.mkdocs_config_path, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
            
        nav = config.get('nav', [])
        
        # Extract all referenced paths from navigation
        nav_paths = self._extract_nav_paths(nav)
        
        # Verify that navigation references point to existing content
        for nav_path in nav_paths:
            if nav_path and nav_path != 'index.md':
                full_path = self.docs_dir / nav_path
                
                # Path should be well-formed
                assert isinstance(nav_path, str), f"Navigation path must be string: {nav_path}"
                
                # If file exists, it should have content
                if full_path.exists():
                    with open(full_path, 'r', encoding='utf-8') as f:
                        content = f.read().strip()
                        assert len(content) > 0, f"Referenced file '{nav_path}' must have content"
                        
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
        
    def test_content_word_count_preservation(self):
        """Test that substantial content is preserved across all folders."""
        total_word_count = 0
        folders_with_content = 0
        
        for folder_name in self.current_folders:
            folder_path = self.docs_dir / folder_name
            if folder_path.exists():
                readme_path = folder_path / "README.md"
                if readme_path.exists():
                    with open(readme_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        word_count = len(content.split())
                        
                        if word_count > 50:  # Substantial content
                            total_word_count += word_count
                            folders_with_content += 1
                            
        # Should have substantial content preserved across multiple folders
        assert folders_with_content >= 20, \
            f"Should have substantial content in at least 20 folders (found {folders_with_content})"
        assert total_word_count >= 10000, \
            f"Should preserve substantial total content (found {total_word_count} words)"
            
    def test_link_preservation_in_content(self):
        """Test that internal and external links are preserved in content."""
        total_links_found = 0
        
        for folder_name in self.current_folders:
            folder_path = self.docs_dir / folder_name
            if folder_path.exists():
                readme_path = folder_path / "README.md"
                if readme_path.exists():
                    with open(readme_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                    # Count markdown links [text](url) and bare URLs
                    markdown_links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
                    bare_urls = re.findall(r'https?://[^\s\)]+', content)
                    
                    folder_links = len(markdown_links) + len(bare_urls)
                    total_links_found += folder_links
                    
        # Should preserve substantial linking between content
        assert total_links_found >= 50, \
            f"Should preserve substantial links in content (found {total_links_found})"
            
    def test_image_references_preservation(self):
        """Test that image references are preserved in content."""
        total_images_found = 0
        
        for folder_name in self.current_folders:
            folder_path = self.docs_dir / folder_name
            if folder_path.exists():
                readme_path = folder_path / "README.md"
                if readme_path.exists():
                    with open(readme_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                    # Count image references ![alt](src) and HTML img tags
                    markdown_images = re.findall(r'!\[([^\]]*)\]\(([^)]+)\)', content)
                    html_images = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content)
                    
                    folder_images = len(markdown_images) + len(html_images)
                    total_images_found += folder_images
                    
        # Should preserve image references (knowledge base has visual content)
        assert total_images_found >= 10, \
            f"Should preserve image references in content (found {total_images_found})"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])