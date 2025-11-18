#!/usr/bin/env python3
"""
HYPERAI Ecosystem Health Diagnostic Tool
==========================================

Comprehensive diagnostic to identify and report ALL issues affecting ecosystem health.
This tool provides SPECIFIC, ACTIONABLE issue reports instead of vague health scores.

Creator: Nguyễn Đức Cường (alpha_prime_omega)
Framework: HYPERAI
Original Creation: October 30, 2025
"""

import os
import sys
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple

class EcosystemHealthDiagnostic:
    """Comprehensive health diagnostic for DAIOF ecosystem"""
    
    def __init__(self):
        self.issues = []
        self.warnings = []
        self.recommendations = []
        self.health_score = 100.0
        
    def add_issue(self, severity: str, category: str, description: str, fix: str = None):
        """Add an issue to the report"""
        issue = {
            'severity': severity,  # CRITICAL, HIGH, MEDIUM, LOW
            'category': category,
            'description': description,
            'fix': fix,
            'timestamp': datetime.utcnow().isoformat()
        }
        self.issues.append(issue)
        
        # Reduce health score based on severity
        severity_impact = {
            'CRITICAL': 20,
            'HIGH': 10,
            'MEDIUM': 5,
            'LOW': 2
        }
        self.health_score -= severity_impact.get(severity, 5)
    
    def check_file_structure(self) -> None:
        """Check for required files and directory structure"""
        print("📁 Checking file structure...")
        
        required_files = {
            'README.md': 'MEDIUM',
            'LICENSE': 'HIGH',
            'CONTRIBUTING.md': 'MEDIUM',
            'SECURITY.md': 'MEDIUM',
            'CODE_OF_CONDUCT.md': 'LOW',
            '.gitignore': 'LOW',
            'requirements.txt': 'MEDIUM',
        }
        
        for file, severity in required_files.items():
            if not Path(file).exists():
                self.add_issue(
                    severity,
                    'file_structure',
                    f'Missing required file: {file}',
                    f'Create {file} with appropriate content'
                )
        
        # Check for test directory
        if not Path('tests').exists():
            self.add_issue(
                'HIGH',
                'file_structure',
                'Missing tests directory',
                'Create tests/ directory with test files'
            )
        elif not list(Path('tests').glob('test_*.py')):
            self.add_issue(
                'MEDIUM',
                'file_structure',
                'Tests directory exists but contains no test files',
                'Add test_*.py files to tests/ directory'
            )
    
    def check_dependencies(self) -> None:
        """Check Python dependencies"""
        print("📦 Checking dependencies...")
        
        if Path('requirements.txt').exists():
            with open('requirements.txt', 'r') as f:
                deps = f.read()
                
            # Check for testing frameworks
            if 'pytest' not in deps and 'unittest' not in deps:
                self.add_issue(
                    'MEDIUM',
                    'dependencies',
                    'No testing framework in requirements.txt',
                    'Add pytest or unittest to requirements.txt'
                )
            
            # Check for common issues
            invalid_deps = []
            for line in deps.split('\n'):
                line = line.strip()
                if line and not line.startswith('#'):
                    # Check if it's a valid package name (not a built-in module)
                    builtin_modules = {'logging', 'hashlib', 'random', 'datetime', 'json', 'pathlib'}
                    pkg_name = line.split('>=')[0].split('==')[0].strip()
                    if pkg_name.lower() in builtin_modules:
                        invalid_deps.append(pkg_name)
            
            if invalid_deps:
                self.add_issue(
                    'LOW',
                    'dependencies',
                    f'Built-in modules listed in requirements.txt: {", ".join(invalid_deps)}',
                    'Remove built-in modules from requirements.txt (they are always available)'
                )
    
    def check_code_quality(self) -> None:
        """Check code quality indicators"""
        print("🔍 Checking code quality...")
        
        # Check for Python files without tests
        python_files = list(Path('.').rglob('*.py'))
        python_files = [f for f in python_files if 'node_modules' not in str(f) and '.git' not in str(f)]
        
        test_files = list(Path('tests').glob('test_*.py')) if Path('tests').exists() else []
        
        if len(python_files) > 5 and len(test_files) == 0:
            self.add_issue(
                'HIGH',
                'code_quality',
                f'Found {len(python_files)} Python files but no test files',
                'Add test files to tests/ directory'
            )
        
        # Check for __pycache__ directories
        pycache_dirs = list(Path('.').rglob('__pycache__'))
        if pycache_dirs:
            self.add_issue(
                'LOW',
                'code_quality',
                f'Found {len(pycache_dirs)} __pycache__ directories in repository',
                'Add __pycache__/ to .gitignore and remove from git'
            )
    
    def check_github_workflows(self) -> None:
        """Check GitHub Actions workflows"""
        print("⚙️ Checking GitHub workflows...")
        
        workflows_dir = Path('.github/workflows')
        if not workflows_dir.exists():
            self.add_issue(
                'MEDIUM',
                'ci_cd',
                'No GitHub workflows directory found',
                'Create .github/workflows/ directory with CI workflow'
            )
            return
        
        workflow_files = list(workflows_dir.glob('*.yml')) + list(workflows_dir.glob('*.yaml'))
        
        if not workflow_files:
            self.add_issue(
                'MEDIUM',
                'ci_cd',
                'GitHub workflows directory exists but contains no workflow files',
                'Add at least one CI workflow (e.g., python-package.yml)'
            )
        
        # Check for test workflow
        has_test_workflow = False
        for wf in workflow_files:
            content = wf.read_text()
            if 'pytest' in content or 'python -m unittest' in content or 'test' in wf.name.lower():
                has_test_workflow = True
                break
        
        if not has_test_workflow and workflow_files:
            self.add_issue(
                'MEDIUM',
                'ci_cd',
                'No test workflow found in GitHub Actions',
                'Add a workflow that runs tests (e.g., pytest or unittest)'
            )
    
    def check_documentation(self) -> None:
        """Check documentation quality"""
        print("📚 Checking documentation...")
        
        if Path('README.md').exists():
            readme_content = Path('README.md').read_text()
            
            # Check README length
            if len(readme_content) < 500:
                self.add_issue(
                    'LOW',
                    'documentation',
                    'README.md is very short (< 500 characters)',
                    'Expand README with more details about the project'
                )
            
            # Check for essential README sections
            essential_sections = ['installation', 'usage', 'license']
            missing_sections = [s for s in essential_sections if s not in readme_content.lower()]
            
            if missing_sections:
                self.add_issue(
                    'LOW',
                    'documentation',
                    f'README missing sections: {", ".join(missing_sections)}',
                    'Add missing sections to README.md'
                )
    
    def check_git_hygiene(self) -> None:
        """Check git repository hygiene"""
        print("🧹 Checking git hygiene...")
        
        if Path('.git').exists():
            # Check .gitignore
            if Path('.gitignore').exists():
                gitignore_content = Path('.gitignore').read_text()
                
                important_ignores = ['__pycache__', '*.pyc', '.env', 'venv/', 'node_modules/']
                missing_ignores = [ig for ig in important_ignores if ig not in gitignore_content]
                
                if missing_ignores:
                    self.add_issue(
                        'LOW',
                        'git_hygiene',
                        f'.gitignore missing important patterns: {", ".join(missing_ignores)}',
                        'Add missing patterns to .gitignore'
                    )
    
    def check_security(self) -> None:
        """Check for security issues"""
        print("🔒 Checking security...")
        
        # Check for exposed secrets
        sensitive_patterns = ['.env', 'secrets', 'password', 'api_key', 'token']
        
        for py_file in Path('.').rglob('*.py'):
            if 'node_modules' in str(py_file) or '.git' in str(py_file):
                continue
            
            try:
                content = py_file.read_text()
                for pattern in sensitive_patterns:
                    if pattern in content.lower() and '=' in content:
                        # Simple heuristic to detect potential secrets
                        if f'{pattern}' in content.lower():
                            self.add_issue(
                                'LOW',
                                'security',
                                f'Potential sensitive data reference in {py_file.name}',
                                'Review file to ensure no secrets are hardcoded'
                            )
                            break
            except:
                pass
    
    def run_full_diagnostic(self) -> Dict:
        """Run all diagnostic checks"""
        print("=" * 80)
        print("🔍 HYPERAI ECOSYSTEM HEALTH DIAGNOSTIC")
        print("=" * 80)
        print(f"Timestamp: {datetime.utcnow().isoformat()}")
        print(f"Creator: Nguyễn Đức Cường (alpha_prime_omega)")
        print(f"Framework: HYPERAI")
        print("=" * 80)
        print()
        
        # Run all checks
        self.check_file_structure()
        self.check_dependencies()
        self.check_code_quality()
        self.check_github_workflows()
        self.check_documentation()
        self.check_git_hygiene()
        self.check_security()
        
        # Ensure health score doesn't go below 0
        self.health_score = max(0.0, min(100.0, self.health_score))
        
        return self.generate_report()
    
    def generate_report(self) -> Dict:
        """Generate comprehensive health report"""
        print()
        print("=" * 80)
        print("📊 DIAGNOSTIC RESULTS")
        print("=" * 80)
        
        # Group issues by severity
        critical = [i for i in self.issues if i['severity'] == 'CRITICAL']
        high = [i for i in self.issues if i['severity'] == 'HIGH']
        medium = [i for i in self.issues if i['severity'] == 'MEDIUM']
        low = [i for i in self.issues if i['severity'] == 'LOW']
        
        print(f"\n🏥 Overall Health Score: {self.health_score:.1f}%")
        print(f"📋 Total Issues Found: {len(self.issues)}")
        print(f"   🔴 Critical: {len(critical)}")
        print(f"   🟠 High: {len(high)}")
        print(f"   🟡 Medium: {len(medium)}")
        print(f"   🟢 Low: {len(low)}")
        
        # Print issues by severity
        for severity, issues in [('CRITICAL', critical), ('HIGH', high), ('MEDIUM', medium), ('LOW', low)]:
            if issues:
                print(f"\n{severity} Issues:")
                for idx, issue in enumerate(issues, 1):
                    print(f"  {idx}. [{issue['category']}] {issue['description']}")
                    if issue['fix']:
                        print(f"     Fix: {issue['fix']}")
        
        report = {
            'timestamp': datetime.utcnow().isoformat(),
            'health_score': self.health_score,
            'total_issues': len(self.issues),
            'issues_by_severity': {
                'critical': len(critical),
                'high': len(high),
                'medium': len(medium),
                'low': len(low)
            },
            'issues': self.issues,
            'attribution': 'Nguyễn Đức Cường (alpha_prime_omega)',
            'framework': 'HYPERAI'
        }
        
        # Save report
        report_dir = Path('metrics')
        report_dir.mkdir(exist_ok=True)
        
        report_file = report_dir / f'ecosystem_health_diagnostic_{datetime.utcnow().strftime("%Y%m%d_%H%M%S")}.json'
        with open(report_file, 'w') as f:
            json.dump(report, f, indent=2)
        
        print(f"\n💾 Report saved: {report_file}")
        print("=" * 80)
        
        return report

def main():
    """Main entry point"""
    diagnostic = EcosystemHealthDiagnostic()
    report = diagnostic.run_full_diagnostic()
    
    # Exit with appropriate code
    if report['health_score'] < 50:
        print("\n❌ CRITICAL: Health score below 50% - immediate action required!")
        sys.exit(1)
    elif report['health_score'] < 80:
        print("\n⚠️  WARNING: Health score below 80% - improvements needed")
        sys.exit(0)
    else:
        print("\n✅ SUCCESS: Health score above 80% - ecosystem is healthy!")
        sys.exit(0)

if __name__ == '__main__':
    main()
